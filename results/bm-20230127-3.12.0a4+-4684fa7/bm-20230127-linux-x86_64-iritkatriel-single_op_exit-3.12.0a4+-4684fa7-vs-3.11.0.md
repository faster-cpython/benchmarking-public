
# Results vs. 3.11.0

- fork: iritkatriel
- ref: single_op_exit
- machine: linux-x86_64
- commit hash: 4684fa7
- commit date: 2023-01-27
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 251 ms: 1.03x faster                                                  |
| chameleon      | 6.41 ms                                                | 6.53 ms: 1.02x slower                                                 |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                |
| html5lib       | 63.2 ms                                                | 60.1 ms: 1.05x faster                                                 |
| tornado_http   | 96.6 ms                                                | 93.0 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                                  |
| float          | 76.3 ms                                                | 72.8 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                  |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                                  |
| regex_effbot   | 3.36 ms                                                | 3.57 ms: 1.06x slower                                                 |
| regex_v8       | 22.3 ms                                                | 25.9 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.28 ms: 1.36x faster                                                 |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                                  |
| json_loads           | 26.2 us                                                | 24.1 us: 1.09x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                  |
| pickle_pure_python   | 304 us                                                 | 283 us: 1.07x faster                                                  |
| pickle_dict          | 31.4 us                                                | 31.1 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.01x faster                                                  |
| unpickle_list        | 4.95 us                                                | 4.98 us: 1.00x slower                                                 |
| xml_etree_process    | 53.8 ms                                                | 54.1 ms: 1.01x slower                                                 |
| pickle_list          | 4.17 us                                                | 4.21 us: 1.01x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 77.6 ms: 1.02x slower                                                 |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.96 ms: 1.07x slower                                                 |
| python_startup_no_site | 5.96 ms                                                | 6.48 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 46.1 ms: 1.13x faster                                                 |
| genshi_text    | 22.1 ms                                                | 20.4 ms: 1.08x faster                                                 |
| mako           | 9.85 ms                                                | 9.69 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.28 ms: 1.36x faster                                                 |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                                  |
| genshi_xml              | 52.1 ms                                                | 46.1 ms: 1.13x faster                                                 |
| deltablue               | 3.64 ms                                                | 3.26 ms: 1.12x faster                                                 |
| nqueens                 | 85.0 ms                                                | 76.8 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.99 ms: 1.10x faster                                                 |
| richards                | 46.2 ms                                                | 42.1 ms: 1.10x faster                                                 |
| scimark_fft             | 329 ms                                                 | 301 ms: 1.09x faster                                                  |
| json_loads              | 26.2 us                                                | 24.1 us: 1.09x faster                                                 |
| genshi_text             | 22.1 ms                                                | 20.4 ms: 1.08x faster                                                 |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                  |
| pickle_pure_python      | 304 us                                                 | 283 us: 1.07x faster                                                  |
| sympy_sum               | 166 ms                                                 | 154 ms: 1.07x faster                                                  |
| json                    | 4.95 ms                                                | 4.61 ms: 1.07x faster                                                 |
| pycparser               | 1.17 sec                                               | 1.09 sec: 1.07x faster                                                |
| sympy_str               | 287 ms                                                 | 268 ms: 1.07x faster                                                  |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                  |
| logging_silent          | 98.5 ns                                                | 92.0 ns: 1.07x faster                                                 |
| hexiom                  | 6.35 ms                                                | 5.94 ms: 1.07x faster                                                 |
| scimark_monte_carlo     | 68.3 ms                                                | 64.2 ms: 1.06x faster                                                 |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                  |
| logging_simple          | 6.06 us                                                | 5.70 us: 1.06x faster                                                 |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.06x faster                                                 |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                                 |
| chaos                   | 68.6 ms                                                | 64.8 ms: 1.06x faster                                                 |
| logging_format          | 6.62 us                                                | 6.25 us: 1.06x faster                                                 |
| aiohttp                 | 1.05 ms                                                | 991 us: 1.06x faster                                                  |
| telco                   | 6.62 ms                                                | 6.28 ms: 1.05x faster                                                 |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                                  |
| bench_thread_pool       | 810 us                                                 | 769 us: 1.05x faster                                                  |
| deepcopy                | 344 us                                                 | 327 us: 1.05x faster                                                  |
| html5lib                | 63.2 ms                                                | 60.1 ms: 1.05x faster                                                 |
| coroutines              | 26.1 ms                                                | 24.8 ms: 1.05x faster                                                 |
| deepcopy_memo           | 36.4 us                                                | 34.7 us: 1.05x faster                                                 |
| float                   | 76.3 ms                                                | 72.8 ms: 1.05x faster                                                 |
| go                      | 143 ms                                                 | 137 ms: 1.05x faster                                                  |
| sqlglot_optimize        | 53.0 ms                                                | 50.6 ms: 1.05x faster                                                 |
| sympy_expand            | 472 ms                                                 | 452 ms: 1.05x faster                                                  |
| pyflate                 | 417 ms                                                 | 399 ms: 1.05x faster                                                  |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.04x faster                                                |
| tornado_http            | 96.6 ms                                                | 93.0 ms: 1.04x faster                                                 |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                |
| spectral_norm           | 99.9 ms                                                | 96.5 ms: 1.04x faster                                                 |
| raytrace                | 290 ms                                                 | 281 ms: 1.03x faster                                                  |
| dulwich_log             | 63.9 ms                                                | 61.8 ms: 1.03x faster                                                 |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                                  |
| coverage                | 101 ms                                                 | 97.8 ms: 1.03x faster                                                 |
| 2to3                    | 257 ms                                                 | 251 ms: 1.03x faster                                                  |
| pprint_safe_repr        | 691 ms                                                 | 674 ms: 1.03x faster                                                  |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                 |
| mako                    | 9.85 ms                                                | 9.69 ms: 1.02x faster                                                 |
| unpack_sequence         | 43.4 ns                                                | 42.8 ns: 1.01x faster                                                 |
| deepcopy_reduce         | 2.97 us                                                | 2.93 us: 1.01x faster                                                 |
| async_generators        | 359 ms                                                 | 354 ms: 1.01x faster                                                  |
| pickle_dict             | 31.4 us                                                | 31.1 us: 1.01x faster                                                 |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.01x faster                                                  |
| scimark_lu              | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| crypto_pyaes            | 73.9 ms                                                | 73.3 ms: 1.01x faster                                                 |
| unpickle_list           | 4.95 us                                                | 4.98 us: 1.00x slower                                                 |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                |
| xml_etree_process       | 53.8 ms                                                | 54.1 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed | 752 ms                                                 | 757 ms: 1.01x slower                                                  |
| pickle_list             | 4.17 us                                                | 4.21 us: 1.01x slower                                                 |
| xml_etree_generate      | 76.2 ms                                                | 77.6 ms: 1.02x slower                                                 |
| chameleon               | 6.41 ms                                                | 6.53 ms: 1.02x slower                                                 |
| mdp                     | 2.62 sec                                               | 2.69 sec: 1.02x slower                                                |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                                  |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                 |
| sqlite_synth            | 2.49 us                                                | 2.57 us: 1.03x slower                                                 |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                 |
| generators              | 72.2 ms                                                | 74.9 ms: 1.04x slower                                                 |
| regex_effbot            | 3.36 ms                                                | 3.57 ms: 1.06x slower                                                 |
| python_startup          | 8.36 ms                                                | 8.96 ms: 1.07x slower                                                 |
| python_startup_no_site  | 5.96 ms                                                | 6.48 ms: 1.09x slower                                                 |
| regex_v8                | 22.3 ms                                                | 25.9 ms: 1.16x slower                                                 |
| mypy                    | 669 ms                                                 | 802 ms: 1.20x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (8): async_tree_none, bench_mp_pool, nbody, django_template, meteor_contest, thrift, unpickle, async_tree_memoization
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230127-3.12.0a4+-4684fa7/bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
