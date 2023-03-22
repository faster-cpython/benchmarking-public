
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3adb23a
- commit date: 2023-03-18
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 165 ms: 1.02x slower                                   |
| chameleon      | 4.57 ms                                                | 4.48 ms: 1.02x faster                                  |
| docutils       | 1.47 sec                                               | 1.51 sec: 1.03x slower                                 |
| html5lib       | 34.7 ms                                                | 35.7 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 60.7 ms: 1.08x faster                                  |
| float          | 53.0 ms                                                | 52.7 ms: 1.01x faster                                  |
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.9 ms: 1.01x faster                                  |
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.01x faster                                  |
| regex_effbot   | 2.63 ms                                                | 2.68 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.28 ms: 1.23x faster                                  |
| unpickle_pure_python | 159 us                                                 | 145 us: 1.09x faster                                   |
| xml_etree_parse      | 106 ms                                                 | 97.4 ms: 1.09x faster                                  |
| pickle_pure_python   | 199 us                                                 | 192 us: 1.04x faster                                   |
| unpickle_list        | 2.63 us                                                | 2.64 us: 1.00x slower                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 70.3 ms: 1.02x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.02x slower                                  |
| pickle               | 7.17 us                                                | 7.41 us: 1.03x slower                                  |
| xml_etree_process    | 35.2 ms                                                | 36.7 ms: 1.04x slower                                  |
| xml_etree_generate   | 48.8 ms                                                | 51.8 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.5 ms                                                | 11.0 ms: 1.05x faster                                  |
| python_startup_no_site | 9.31 ms                                                | 8.99 ms: 1.04x faster                                  |
| Geometric mean         | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.44 ms: 1.14x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.8 ms: 1.03x faster                                  |
| genshi_xml      | 29.8 ms                                                | 29.3 ms: 1.02x faster                                  |
| django_template | 21.0 ms                                                | 21.9 ms: 1.04x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 449 ms: 1.45x faster                                   |
| json_dumps              | 7.72 ms                                                | 6.28 ms: 1.23x faster                                  |
| mako                    | 8.49 ms                                                | 7.44 ms: 1.14x faster                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.86 ms: 1.12x faster                                  |
| deltablue               | 2.81 ms                                                | 2.56 ms: 1.10x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 145 us: 1.09x faster                                   |
| xml_etree_parse         | 106 ms                                                 | 97.4 ms: 1.09x faster                                  |
| nbody                   | 65.5 ms                                                | 60.7 ms: 1.08x faster                                  |
| hexiom                  | 4.73 ms                                                | 4.40 ms: 1.07x faster                                  |
| scimark_fft             | 199 ms                                                 | 187 ms: 1.06x faster                                   |
| python_startup          | 11.5 ms                                                | 11.0 ms: 1.05x faster                                  |
| richards                | 32.2 ms                                                | 30.7 ms: 1.05x faster                                  |
| coverage                | 58.6 ms                                                | 56.0 ms: 1.05x faster                                  |
| chaos                   | 49.5 ms                                                | 47.4 ms: 1.04x faster                                  |
| generators              | 28.8 ms                                                | 27.8 ms: 1.04x faster                                  |
| python_startup_no_site  | 9.31 ms                                                | 8.99 ms: 1.04x faster                                  |
| pickle_pure_python      | 199 us                                                 | 192 us: 1.04x faster                                   |
| mdp                     | 1.54 sec                                               | 1.49 sec: 1.03x faster                                 |
| create_gc_cycles        | 726 us                                                 | 705 us: 1.03x faster                                   |
| pycparser               | 697 ms                                                 | 676 ms: 1.03x faster                                   |
| genshi_text             | 15.3 ms                                                | 14.8 ms: 1.03x faster                                  |
| chameleon               | 4.57 ms                                                | 4.48 ms: 1.02x faster                                  |
| deepcopy_memo           | 26.3 us                                                | 25.8 us: 1.02x faster                                  |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.19 ms: 1.02x faster                                  |
| logging_silent          | 68.0 ns                                                | 66.9 ns: 1.02x faster                                  |
| genshi_xml              | 29.8 ms                                                | 29.3 ms: 1.02x faster                                  |
| scimark_lu              | 72.1 ms                                                | 71.2 ms: 1.01x faster                                  |
| regex_compile           | 76.7 ms                                                | 75.9 ms: 1.01x faster                                  |
| spectral_norm           | 72.8 ms                                                | 72.1 ms: 1.01x faster                                  |
| dulwich_log             | 29.9 ms                                                | 29.6 ms: 1.01x faster                                  |
| unpack_sequence         | 33.6 ns                                                | 33.3 ns: 1.01x faster                                  |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.01x faster                                  |
| float                   | 53.0 ms                                                | 52.7 ms: 1.01x faster                                  |
| deepcopy                | 224 us                                                 | 222 us: 1.01x faster                                   |
| gc_traversal            | 2.43 ms                                                | 2.43 ms: 1.00x faster                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| unpickle_list           | 2.63 us                                                | 2.64 us: 1.00x slower                                  |
| fannkuch                | 261 ms                                                 | 262 ms: 1.01x slower                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                  |
| json                    | 2.77 ms                                                | 2.80 ms: 1.01x slower                                  |
| async_tree_none         | 285 ms                                                 | 288 ms: 1.01x slower                                   |
| xml_etree_iterparse     | 69.2 ms                                                | 70.3 ms: 1.02x slower                                  |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                   |
| json_loads              | 16.1 us                                                | 16.3 us: 1.02x slower                                  |
| pprint_pformat          | 950 ms                                                 | 967 ms: 1.02x slower                                   |
| regex_effbot            | 2.63 ms                                                | 2.68 ms: 1.02x slower                                  |
| sympy_str               | 152 ms                                                 | 154 ms: 1.02x slower                                   |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.02x slower                                  |
| sympy_expand            | 243 ms                                                 | 248 ms: 1.02x slower                                   |
| coroutines              | 17.7 ms                                                | 18.1 ms: 1.02x slower                                  |
| pprint_safe_repr        | 465 ms                                                 | 475 ms: 1.02x slower                                   |
| go                      | 109 ms                                                 | 111 ms: 1.02x slower                                   |
| 2to3                    | 161 ms                                                 | 165 ms: 1.02x slower                                   |
| docutils                | 1.47 sec                                               | 1.51 sec: 1.03x slower                                 |
| deepcopy_reduce         | 1.91 us                                                | 1.96 us: 1.03x slower                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 548 ms: 1.03x slower                                   |
| sqlglot_optimize        | 31.2 ms                                                | 32.0 ms: 1.03x slower                                  |
| sympy_sum               | 86.0 ms                                                | 88.3 ms: 1.03x slower                                  |
| scimark_sor             | 83.0 ms                                                | 85.2 ms: 1.03x slower                                  |
| sqlalchemy_declarative  | 62.7 ms                                                | 64.5 ms: 1.03x slower                                  |
| telco                   | 3.39 ms                                                | 3.49 ms: 1.03x slower                                  |
| html5lib                | 34.7 ms                                                | 35.7 ms: 1.03x slower                                  |
| pickle                  | 7.17 us                                                | 7.41 us: 1.03x slower                                  |
| bench_mp_pool           | 43.2 ms                                                | 44.8 ms: 1.04x slower                                  |
| django_template         | 21.0 ms                                                | 21.9 ms: 1.04x slower                                  |
| xml_etree_process       | 35.2 ms                                                | 36.7 ms: 1.04x slower                                  |
| logging_format          | 3.78 us                                                | 3.95 us: 1.05x slower                                  |
| logging_simple          | 3.50 us                                                | 3.66 us: 1.05x slower                                  |
| thrift                  | 433 us                                                 | 456 us: 1.05x slower                                   |
| async_tree_io           | 706 ms                                                 | 743 ms: 1.05x slower                                   |
| crypto_pyaes            | 51.7 ms                                                | 54.6 ms: 1.05x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.35 us: 1.06x slower                                  |
| xml_etree_generate      | 48.8 ms                                                | 51.8 ms: 1.06x slower                                  |
| pyflate                 | 311 ms                                                 | 332 ms: 1.07x slower                                   |
| raytrace                | 207 ms                                                 | 222 ms: 1.07x slower                                   |
| scimark_monte_carlo     | 46.4 ms                                                | 50.7 ms: 1.09x slower                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.23 ms: 1.10x slower                                  |
| sqlglot_parse           | 957 us                                                 | 1.06 ms: 1.10x slower                                  |
| comprehensions          | 16.1 us                                                | 17.9 us: 1.11x slower                                  |
| async_generators        | 195 ms                                                 | 266 ms: 1.36x slower                                   |
| dask                    | 226 ms                                                 | 322 ms: 1.42x slower                                   |
| Geometric mean          | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (9): tornado_http, async_tree_memoization, bench_thread_pool, regex_dna, meteor_contest, pathlib, nqueens, unpickle, mypy2
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint
