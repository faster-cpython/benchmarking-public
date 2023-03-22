
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.21x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 335 ms                                                 | 264 ms: 1.27x faster                                  |
| chameleon      | 9.17 ms                                                | 7.44 ms: 1.23x faster                                 |
| html5lib       | 85.9 ms                                                | 68.5 ms: 1.25x faster                                 |
| tornado_http   | 128 ms                                                 | 108 ms: 1.19x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 144 ms                                                 | 96.1 ms: 1.50x faster                                 |
| float          | 109 ms                                                 | 79.2 ms: 1.38x faster                                 |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 139 ms: 1.28x faster                                  |
| regex_v8       | 25.0 ms                                                | 24.5 ms: 1.02x faster                                 |
| regex_dna      | 214 ms                                                 | 212 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 347 us: 1.30x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 57.8 ms: 1.29x faster                                 |
| unpickle_pure_python | 302 us                                                 | 251 us: 1.20x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 80.8 ms: 1.16x faster                                 |
| json_loads           | 28.7 us                                                | 25.6 us: 1.12x faster                                 |
| json_dumps           | 13.4 ms                                                | 12.6 ms: 1.07x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.05x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.05x faster                                  |
| pickle               | 10.2 us                                                | 9.95 us: 1.02x faster                                 |
| pickle_list          | 4.72 us                                                | 4.68 us: 1.01x faster                                 |
| pickle_dict          | 27.6 us                                                | 27.7 us: 1.00x slower                                 |
| unpickle             | 14.2 us                                                | 14.6 us: 1.03x slower                                 |
| unpickle_list        | 4.92 us                                                | 5.21 us: 1.06x slower                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.00 ms: 1.76x faster                                 |
| python_startup_no_site | 5.78 ms                                                | 5.78 ms: 1.00x slower                                 |
| Geometric mean         | (ref)                                                  | 1.33x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 46.3 ms                                                | 36.5 ms: 1.27x faster                                 |
| mako            | 14.7 ms                                                | 11.9 ms: 1.23x faster                                 |
| Geometric mean  | (ref)                                                  | 1.25x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup          | 14.1 ms                                                | 8.00 ms: 1.76x faster                                 |
| deltablue               | 7.28 ms                                                | 4.54 ms: 1.60x faster                                 |
| logging_silent          | 176 ns                                                 | 110 ns: 1.60x faster                                  |
| scimark_sor             | 197 ms                                                 | 130 ms: 1.51x faster                                  |
| nbody                   | 144 ms                                                 | 96.1 ms: 1.50x faster                                 |
| scimark_monte_carlo     | 109 ms                                                 | 74.0 ms: 1.47x faster                                 |
| spectral_norm           | 150 ms                                                 | 104 ms: 1.45x faster                                  |
| scimark_lu              | 161 ms                                                 | 112 ms: 1.44x faster                                  |
| go                      | 226 ms                                                 | 158 ms: 1.43x faster                                  |
| chaos                   | 106 ms                                                 | 73.9 ms: 1.43x faster                                 |
| pyflate                 | 676 ms                                                 | 477 ms: 1.42x faster                                  |
| raytrace                | 467 ms                                                 | 333 ms: 1.40x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.77 ms: 1.39x faster                                 |
| richards                | 75.2 ms                                                | 54.5 ms: 1.38x faster                                 |
| float                   | 109 ms                                                 | 79.2 ms: 1.38x faster                                 |
| logging_format          | 8.85 us                                                | 6.49 us: 1.36x faster                                 |
| logging_simple          | 8.10 us                                                | 5.97 us: 1.36x faster                                 |
| crypto_pyaes            | 117 ms                                                 | 88.1 ms: 1.32x faster                                 |
| pickle_pure_python      | 452 us                                                 | 347 us: 1.30x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 57.8 ms: 1.29x faster                                 |
| regex_compile           | 177 ms                                                 | 139 ms: 1.28x faster                                  |
| 2to3                    | 335 ms                                                 | 264 ms: 1.27x faster                                  |
| thrift                  | 1.03 ms                                                | 814 us: 1.27x faster                                  |
| django_template         | 46.3 ms                                                | 36.5 ms: 1.27x faster                                 |
| scimark_fft             | 421 ms                                                 | 332 ms: 1.27x faster                                  |
| fannkuch                | 488 ms                                                 | 386 ms: 1.26x faster                                  |
| html5lib                | 85.9 ms                                                | 68.5 ms: 1.25x faster                                 |
| pycparser               | 1.53 sec                                               | 1.24 sec: 1.24x faster                                |
| chameleon               | 9.17 ms                                                | 7.44 ms: 1.23x faster                                 |
| mako                    | 14.7 ms                                                | 11.9 ms: 1.23x faster                                 |
| unpack_sequence         | 59.4 ns                                                | 49.2 ns: 1.21x faster                                 |
| unpickle_pure_python    | 302 us                                                 | 251 us: 1.20x faster                                  |
| tornado_http            | 128 ms                                                 | 108 ms: 1.19x faster                                  |
| nqueens                 | 100 ms                                                 | 84.6 ms: 1.18x faster                                 |
| xml_etree_generate      | 93.8 ms                                                | 80.8 ms: 1.16x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.77 ms: 1.14x faster                                 |
| dulwich_log             | 75.8 ms                                                | 67.2 ms: 1.13x faster                                 |
| json_loads              | 28.7 us                                                | 25.6 us: 1.12x faster                                 |
| json                    | 5.35 ms                                                | 4.83 ms: 1.11x faster                                 |
| sympy_integrate         | 24.0 ms                                                | 21.7 ms: 1.11x faster                                 |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.74 us: 1.07x faster                                 |
| sympy_sum               | 183 ms                                                 | 172 ms: 1.07x faster                                  |
| json_dumps              | 13.4 ms                                                | 12.6 ms: 1.07x faster                                 |
| sympy_str               | 325 ms                                                 | 308 ms: 1.05x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.05x faster                                  |
| sympy_expand            | 534 ms                                                 | 509 ms: 1.05x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.05x faster                                  |
| pathlib                 | 20.0 ms                                                | 19.4 ms: 1.03x faster                                 |
| telco                   | 6.73 ms                                                | 6.56 ms: 1.03x faster                                 |
| regex_v8                | 25.0 ms                                                | 24.5 ms: 1.02x faster                                 |
| pickle                  | 10.2 us                                                | 9.95 us: 1.02x faster                                 |
| pickle_list             | 4.72 us                                                | 4.68 us: 1.01x faster                                 |
| regex_dna               | 214 ms                                                 | 212 ms: 1.01x faster                                  |
| python_startup_no_site  | 5.78 ms                                                | 5.78 ms: 1.00x slower                                 |
| pickle_dict             | 27.6 us                                                | 27.7 us: 1.00x slower                                 |
| unpickle                | 14.2 us                                                | 14.6 us: 1.03x slower                                 |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                  |
| unpickle_list           | 4.92 us                                                | 5.21 us: 1.06x slower                                 |
| Geometric mean          | (ref)                                                  | 1.21x faster                                          |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
