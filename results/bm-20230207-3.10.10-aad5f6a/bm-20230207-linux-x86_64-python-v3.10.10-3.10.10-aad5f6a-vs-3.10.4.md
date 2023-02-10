
# Results vs. 3.10.4

- fork: python
- ref: v3.10.10
- machine: linux-x86_64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.00x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 335 ms: 1.01x slower                                     |
| chameleon      | 8.86 ms                                                | 9.13 ms: 1.03x slower                                    |
| docutils       | 3.18 sec                                               | 3.22 sec: 1.01x slower                                   |
| html5lib       | 85.8 ms                                                | 87.5 ms: 1.02x slower                                    |
| tornado_http   | 128 ms                                                 | 130 ms: 1.01x slower                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                     |
| float          | 108 ms                                                 | 109 ms: 1.01x slower                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| regex_v8       | 25.0 ms                                                | 24.1 ms: 1.03x faster                                    |
| regex_dna      | 214 ms                                                 | 216 ms: 1.01x slower                                     |
| regex_compile  | 174 ms                                                 | 177 ms: 1.02x slower                                     |
| regex_effbot   | 3.21 ms                                                | 3.62 ms: 1.13x slower                                    |
| Geometric mean | (ref)                                                  | 1.03x slower                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|--------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| pickle_list        | 4.50 us                                                | 4.17 us: 1.08x faster                                    |
| xml_etree_parse    | 163 ms                                                 | 161 ms: 1.02x faster                                     |
| unpickle_list      | 4.99 us                                                | 4.94 us: 1.01x faster                                    |
| pickle_pure_python | 453 us                                                 | 449 us: 1.01x faster                                     |
| pickle             | 10.1 us                                                | 10.2 us: 1.01x slower                                    |
| json_dumps         | 13.5 ms                                                | 13.6 ms: 1.01x slower                                    |
| json_loads         | 28.9 us                                                | 29.2 us: 1.01x slower                                    |
| unpickle           | 14.3 us                                                | 14.8 us: 1.04x slower                                    |
| pickle_dict        | 28.3 us                                                | 30.5 us: 1.08x slower                                    |
| Geometric mean     | (ref)                                                  | 1.00x slower                                             |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 9.33 ms: 1.49x faster                                    |
| python_startup_no_site | 5.76 ms                                                | 5.79 ms: 1.00x slower                                    |
| Geometric mean         | (ref)                                                  | 1.22x faster                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 30.1 ms: 1.02x faster                                    |
| genshi_xml      | 63.6 ms                                                | 62.6 ms: 1.02x faster                                    |
| django_template | 46.3 ms                                                | 46.6 ms: 1.01x slower                                    |
| mako            | 14.3 ms                                                | 14.6 ms: 1.02x slower                                    |
| Geometric mean  | (ref)                                                  | 1.00x faster                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup          | 13.9 ms                                                | 9.33 ms: 1.49x faster                                    |
| pickle_list             | 4.50 us                                                | 4.17 us: 1.08x faster                                    |
| coverage                | 75.3 ms                                                | 71.5 ms: 1.05x faster                                    |
| aiohttp                 | 1.34 ms                                                | 1.29 ms: 1.03x faster                                    |
| spectral_norm           | 148 ms                                                 | 143 ms: 1.03x faster                                     |
| regex_v8                | 25.0 ms                                                | 24.1 ms: 1.03x faster                                    |
| coroutines              | 31.7 ms                                                | 30.6 ms: 1.03x faster                                    |
| gunicorn                | 1.43 ms                                                | 1.39 ms: 1.03x faster                                    |
| bench_thread_pool       | 943 us                                                 | 919 us: 1.03x faster                                     |
| pyflate                 | 675 ms                                                 | 659 ms: 1.03x faster                                     |
| crypto_pyaes            | 118 ms                                                 | 115 ms: 1.02x faster                                     |
| fannkuch                | 477 ms                                                 | 467 ms: 1.02x faster                                     |
| genshi_text             | 30.6 ms                                                | 30.1 ms: 1.02x faster                                    |
| scimark_sparse_mat_mult | 5.48 ms                                                | 5.39 ms: 1.02x faster                                    |
| genshi_xml              | 63.6 ms                                                | 62.6 ms: 1.02x faster                                    |
| xml_etree_parse         | 163 ms                                                 | 161 ms: 1.02x faster                                     |
| pathlib                 | 20.0 ms                                                | 19.7 ms: 1.01x faster                                    |
| scimark_fft             | 414 ms                                                 | 408 ms: 1.01x faster                                     |
| unpickle_list           | 4.99 us                                                | 4.94 us: 1.01x faster                                    |
| pickle_pure_python      | 453 us                                                 | 449 us: 1.01x faster                                     |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                     |
| meteor_contest          | 114 ms                                                 | 113 ms: 1.01x faster                                     |
| sqlglot_parse           | 2.04 ms                                                | 2.03 ms: 1.01x faster                                    |
| async_generators        | 428 ms                                                 | 426 ms: 1.00x faster                                     |
| deepcopy                | 429 us                                                 | 428 us: 1.00x faster                                     |
| raytrace                | 461 ms                                                 | 463 ms: 1.00x slower                                     |
| python_startup_no_site  | 5.76 ms                                                | 5.79 ms: 1.00x slower                                    |
| generators              | 75.8 ms                                                | 76.1 ms: 1.00x slower                                    |
| sqlglot_normalize       | 135 ms                                                 | 136 ms: 1.01x slower                                     |
| django_template         | 46.3 ms                                                | 46.6 ms: 1.01x slower                                    |
| 2to3                    | 332 ms                                                 | 335 ms: 1.01x slower                                     |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                    |
| json                    | 5.35 ms                                                | 5.40 ms: 1.01x slower                                    |
| json_dumps              | 13.5 ms                                                | 13.6 ms: 1.01x slower                                    |
| nqueens                 | 99.3 ms                                                | 100 ms: 1.01x slower                                     |
| pylint                  | 519 ms                                                 | 524 ms: 1.01x slower                                     |
| flaskblogging           | 8.38 ms                                                | 8.47 ms: 1.01x slower                                    |
| sqlalchemy_declarative  | 165 ms                                                 | 167 ms: 1.01x slower                                     |
| float                   | 108 ms                                                 | 109 ms: 1.01x slower                                     |
| regex_dna               | 214 ms                                                 | 216 ms: 1.01x slower                                     |
| docutils                | 3.18 sec                                               | 3.22 sec: 1.01x slower                                   |
| scimark_lu              | 158 ms                                                 | 160 ms: 1.01x slower                                     |
| json_loads              | 28.9 us                                                | 29.2 us: 1.01x slower                                    |
| tornado_http            | 128 ms                                                 | 130 ms: 1.01x slower                                     |
| sympy_str               | 324 ms                                                 | 329 ms: 1.01x slower                                     |
| regex_compile           | 174 ms                                                 | 177 ms: 1.02x slower                                     |
| deepcopy_reduce         | 3.75 us                                                | 3.81 us: 1.02x slower                                    |
| sympy_expand            | 537 ms                                                 | 546 ms: 1.02x slower                                     |
| richards                | 71.4 ms                                                | 72.6 ms: 1.02x slower                                    |
| pycparser               | 1.51 sec                                               | 1.54 sec: 1.02x slower                                   |
| sympy_integrate         | 23.9 ms                                                | 24.4 ms: 1.02x slower                                    |
| html5lib                | 85.8 ms                                                | 87.5 ms: 1.02x slower                                    |
| chaos                   | 104 ms                                                 | 106 ms: 1.02x slower                                     |
| sqlite_synth            | 2.90 us                                                | 2.97 us: 1.02x slower                                    |
| pprint_pformat          | 1.97 sec                                               | 2.02 sec: 1.02x slower                                   |
| mako                    | 14.3 ms                                                | 14.6 ms: 1.02x slower                                    |
| sympy_sum               | 183 ms                                                 | 189 ms: 1.03x slower                                     |
| chameleon               | 8.86 ms                                                | 9.13 ms: 1.03x slower                                    |
| logging_format          | 8.92 us                                                | 9.20 us: 1.03x slower                                    |
| pprint_safe_repr        | 943 ms                                                 | 975 ms: 1.03x slower                                     |
| unpickle                | 14.3 us                                                | 14.8 us: 1.04x slower                                    |
| logging_simple          | 8.06 us                                                | 8.41 us: 1.04x slower                                    |
| async_tree_cpu_io_mixed | 949 ms                                                 | 997 ms: 1.05x slower                                     |
| unpack_sequence         | 59.5 ns                                                | 64.0 ns: 1.08x slower                                    |
| pickle_dict             | 28.3 us                                                | 30.5 us: 1.08x slower                                    |
| regex_effbot            | 3.21 ms                                                | 3.62 ms: 1.13x slower                                    |
| Geometric mean          | (ref)                                                  | 1.00x slower                                             |

Benchmark hidden because not significant (23): sqlalchemy_imperative, xml_etree_generate, mdp, dulwich_log, scimark_sor, sqlglot_transpile, deepcopy_memo, go, bench_mp_pool, xml_etree_process, hexiom, xml_etree_iterparse, sqlglot_optimize, unpickle_pure_python, scimark_monte_carlo, deltablue, async_tree_memoization, async_tree_io, thrift, telco, nbody, logging_silent, async_tree_none
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: mypy
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20230207-3.10.10-aad5f6a/bm-20230207-linux-x86_64-python-v3.10.10-3.10.10-aad5f6a.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
