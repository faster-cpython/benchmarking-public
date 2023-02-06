
# Results vs. base

- fork: faster-cpython
- ref: normalize_current_ex
- machine: linux-x86_64
- commit hash: 0c3dc7b
- commit date: 2023-02-06
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230203-linux-x86_64-python-433fb3ef08c71b97a0d0-3.12.0a4+-433fb3e | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 251 ms: 1.01x faster                                                             |
| chameleon      | 6.41 ms                                                                | 6.51 ms: 1.02x slower                                                            |
| docutils       | 2.50 sec                                                               | 2.52 sec: 1.01x slower                                                           |
| html5lib       | 59.9 ms                                                                | 61.1 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230203-linux-x86_64-python-433fb3ef08c71b97a0d0-3.12.0a4+-433fb3e | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 72.9 ms                                                                | 72.5 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230203-linux-x86_64-python-433fb3ef08c71b97a0d0-3.12.0a4+-433fb3e | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.54 ms                                                                | 3.36 ms: 1.05x faster                                                            |
| regex_dna      | 211 ms                                                                 | 206 ms: 1.03x faster                                                             |
| regex_compile  | 127 ms                                                                 | 129 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230203-linux-x86_64-python-433fb3ef08c71b97a0d0-3.12.0a4+-433fb3e | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_list        | 5.04 us                                                                | 4.93 us: 1.02x faster                                                            |
| unpickle_pure_python | 198 us                                                                 | 197 us: 1.01x faster                                                             |
| xml_etree_iterparse  | 102 ms                                                                 | 102 ms: 1.01x slower                                                             |
| xml_etree_parse      | 147 ms                                                                 | 148 ms: 1.01x slower                                                             |
| json_dumps           | 9.25 ms                                                                | 9.44 ms: 1.02x slower                                                            |
| xml_etree_generate   | 76.9 ms                                                                | 79.7 ms: 1.04x slower                                                            |
| pickle_dict          | 30.8 us                                                                | 32.0 us: 1.04x slower                                                            |
| xml_etree_process    | 53.0 ms                                                                | 55.2 ms: 1.04x slower                                                            |
| pickle_list          | 4.07 us                                                                | 4.25 us: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (4): json_loads, pickle, pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230203-linux-x86_64-python-433fb3ef08c71b97a0d0-3.12.0a4+-433fb3e | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.47 ms                                                                | 6.48 ms: 1.00x slower                                                            |
| python_startup         | 8.94 ms                                                                | 8.95 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230203-linux-x86_64-python-433fb3ef08c71b97a0d0-3.12.0a4+-433fb3e | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako           | 9.77 ms                                                                | 9.67 ms: 1.01x faster                                                            |
| genshi_xml     | 47.1 ms                                                                | 46.7 ms: 1.01x faster                                                            |
| genshi_text    | 20.7 ms                                                                | 20.9 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20230203-linux-x86_64-python-433fb3ef08c71b97a0d0-3.12.0a4+-433fb3e | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot            | 3.54 ms                                                                | 3.36 ms: 1.05x faster                                                            |
| unpack_sequence         | 43.3 ns                                                                | 41.7 ns: 1.04x faster                                                            |
| regex_dna               | 211 ms                                                                 | 206 ms: 1.03x faster                                                             |
| scimark_monte_carlo     | 66.3 ms                                                                | 64.7 ms: 1.02x faster                                                            |
| scimark_sparse_mat_mult | 4.10 ms                                                                | 4.01 ms: 1.02x faster                                                            |
| unpickle_list           | 5.04 us                                                                | 4.93 us: 1.02x faster                                                            |
| json                    | 4.66 ms                                                                | 4.57 ms: 1.02x faster                                                            |
| chaos                   | 64.6 ms                                                                | 63.4 ms: 1.02x faster                                                            |
| coroutines              | 25.7 ms                                                                | 25.4 ms: 1.01x faster                                                            |
| generators              | 77.5 ms                                                                | 76.6 ms: 1.01x faster                                                            |
| mako                    | 9.77 ms                                                                | 9.67 ms: 1.01x faster                                                            |
| fannkuch                | 372 ms                                                                 | 368 ms: 1.01x faster                                                             |
| telco                   | 6.44 ms                                                                | 6.38 ms: 1.01x faster                                                            |
| genshi_xml              | 47.1 ms                                                                | 46.7 ms: 1.01x faster                                                            |
| crypto_pyaes            | 73.5 ms                                                                | 72.8 ms: 1.01x faster                                                            |
| unpickle_pure_python    | 198 us                                                                 | 197 us: 1.01x faster                                                             |
| 2to3                    | 253 ms                                                                 | 251 ms: 1.01x faster                                                             |
| hexiom                  | 6.00 ms                                                                | 5.97 ms: 1.01x faster                                                            |
| float                   | 72.9 ms                                                                | 72.5 ms: 1.01x faster                                                            |
| go                      | 135 ms                                                                 | 134 ms: 1.00x faster                                                             |
| python_startup_no_site  | 6.47 ms                                                                | 6.48 ms: 1.00x slower                                                            |
| python_startup          | 8.94 ms                                                                | 8.95 ms: 1.00x slower                                                            |
| bench_thread_pool       | 785 us                                                                 | 787 us: 1.00x slower                                                             |
| asyncio_tcp             | 491 ms                                                                 | 493 ms: 1.00x slower                                                             |
| scimark_fft             | 304 ms                                                                 | 305 ms: 1.01x slower                                                             |
| xml_etree_iterparse     | 102 ms                                                                 | 102 ms: 1.01x slower                                                             |
| sqlglot_normalize       | 104 ms                                                                 | 105 ms: 1.01x slower                                                             |
| raytrace                | 279 ms                                                                 | 281 ms: 1.01x slower                                                             |
| genshi_text             | 20.7 ms                                                                | 20.9 ms: 1.01x slower                                                            |
| sqlglot_transpile       | 1.70 ms                                                                | 1.72 ms: 1.01x slower                                                            |
| sqlglot_parse           | 1.41 ms                                                                | 1.42 ms: 1.01x slower                                                            |
| xml_etree_parse         | 147 ms                                                                 | 148 ms: 1.01x slower                                                             |
| docutils                | 2.50 sec                                                               | 2.52 sec: 1.01x slower                                                           |
| sqlite_synth            | 2.58 us                                                                | 2.60 us: 1.01x slower                                                            |
| dulwich_log             | 62.4 ms                                                                | 63.1 ms: 1.01x slower                                                            |
| sympy_str               | 269 ms                                                                 | 272 ms: 1.01x slower                                                             |
| scimark_lu              | 108 ms                                                                 | 109 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed | 752 ms                                                                 | 760 ms: 1.01x slower                                                             |
| sympy_integrate         | 19.7 ms                                                                | 20.0 ms: 1.01x slower                                                            |
| deepcopy_reduce         | 2.87 us                                                                | 2.90 us: 1.01x slower                                                            |
| pathlib                 | 17.7 ms                                                                | 17.9 ms: 1.01x slower                                                            |
| create_gc_cycles        | 1.46 ms                                                                | 1.48 ms: 1.01x slower                                                            |
| mdp                     | 2.48 sec                                                               | 2.51 sec: 1.01x slower                                                           |
| deepcopy                | 325 us                                                                 | 329 us: 1.02x slower                                                             |
| chameleon               | 6.41 ms                                                                | 6.51 ms: 1.02x slower                                                            |
| pprint_pformat          | 1.38 sec                                                               | 1.40 sec: 1.02x slower                                                           |
| sympy_expand            | 452 ms                                                                 | 459 ms: 1.02x slower                                                             |
| pycparser               | 1.09 sec                                                               | 1.11 sec: 1.02x slower                                                           |
| regex_compile           | 127 ms                                                                 | 129 ms: 1.02x slower                                                             |
| sympy_sum               | 155 ms                                                                 | 158 ms: 1.02x slower                                                             |
| scimark_sor             | 106 ms                                                                 | 108 ms: 1.02x slower                                                             |
| html5lib                | 59.9 ms                                                                | 61.1 ms: 1.02x slower                                                            |
| json_dumps              | 9.25 ms                                                                | 9.44 ms: 1.02x slower                                                            |
| spectral_norm           | 93.4 ms                                                                | 95.9 ms: 1.03x slower                                                            |
| logging_simple          | 5.71 us                                                                | 5.88 us: 1.03x slower                                                            |
| logging_silent          | 90.4 ns                                                                | 93.2 ns: 1.03x slower                                                            |
| pprint_safe_repr        | 667 ms                                                                 | 689 ms: 1.03x slower                                                             |
| xml_etree_generate      | 76.9 ms                                                                | 79.7 ms: 1.04x slower                                                            |
| logging_format          | 6.25 us                                                                | 6.48 us: 1.04x slower                                                            |
| pickle_dict             | 30.8 us                                                                | 32.0 us: 1.04x slower                                                            |
| xml_etree_process       | 53.0 ms                                                                | 55.2 ms: 1.04x slower                                                            |
| gc_traversal            | 3.65 ms                                                                | 3.82 ms: 1.04x slower                                                            |
| pickle_list             | 4.07 us                                                                | 4.25 us: 1.05x slower                                                            |
| async_generators        | 350 ms                                                                 | 424 ms: 1.21x slower                                                             |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (27): async_tree_memoization, nbody, meteor_contest, coverage, django_template, regex_v8, json_loads, pyflate, aiohttp, pickle, bench_mp_pool, pidigits, richards, pickle_pure_python, sqlglot_optimize, deltablue, djangocms, gunicorn, unpickle, mypy, dask, nqueens, async_tree_io, thrift, tornado_http, deepcopy_memo, async_tree_none
