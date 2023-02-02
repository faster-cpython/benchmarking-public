
# Results vs. base

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 933012e
- commit date: 2023-01-18
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 249 ms: 1.01x faster                                                        |
| docutils       | 2.49 sec                                                               | 2.48 sec: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                                 | 189 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.7 ms                                                                | 21.2 ms: 1.02x faster                                                       |
| regex_dna      | 205 ms                                                                 | 207 ms: 1.01x slower                                                        |
| regex_effbot   | 3.48 ms                                                                | 3.51 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps          | 9.45 ms                                                                | 9.32 ms: 1.01x faster                                                       |
| xml_etree_iterparse | 104 ms                                                                 | 102 ms: 1.01x faster                                                        |
| pickle_pure_python  | 283 us                                                                 | 280 us: 1.01x faster                                                        |
| xml_etree_parse     | 149 ms                                                                 | 148 ms: 1.01x faster                                                        |
| pickle_dict         | 31.2 us                                                                | 31.6 us: 1.01x slower                                                       |
| xml_etree_process   | 53.2 ms                                                                | 54.1 ms: 1.02x slower                                                       |
| xml_etree_generate  | 77.0 ms                                                                | 78.5 ms: 1.02x slower                                                       |
| pickle_list         | 4.02 us                                                                | 4.21 us: 1.05x slower                                                       |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (5): unpickle_pure_python, unpickle_list, pickle, unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.49 ms                                                                | 6.39 ms: 1.02x faster                                                       |
| python_startup         | 8.98 ms                                                                | 8.85 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 20.7 ms                                                                | 20.0 ms: 1.03x faster                                                       |
| django_template | 32.7 ms                                                                | 32.3 ms: 1.01x faster                                                       |
| genshi_xml      | 45.8 ms                                                                | 46.0 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal            | 3.82 ms                                                                | 3.51 ms: 1.09x faster                                                       |
| mdp                     | 2.59 sec                                                               | 2.44 sec: 1.06x faster                                                      |
| unpack_sequence         | 46.3 ns                                                                | 44.0 ns: 1.05x faster                                                       |
| chaos                   | 66.3 ms                                                                | 63.3 ms: 1.05x faster                                                       |
| pidigits                | 198 ms                                                                 | 189 ms: 1.04x faster                                                        |
| generators              | 79.3 ms                                                                | 76.0 ms: 1.04x faster                                                       |
| logging_simple          | 5.82 us                                                                | 5.62 us: 1.04x faster                                                       |
| genshi_text             | 20.7 ms                                                                | 20.0 ms: 1.03x faster                                                       |
| logging_silent          | 93.3 ns                                                                | 90.4 ns: 1.03x faster                                                       |
| logging_format          | 6.38 us                                                                | 6.18 us: 1.03x faster                                                       |
| scimark_sparse_mat_mult | 4.08 ms                                                                | 3.96 ms: 1.03x faster                                                       |
| telco                   | 6.60 ms                                                                | 6.42 ms: 1.03x faster                                                       |
| regex_v8                | 21.7 ms                                                                | 21.2 ms: 1.02x faster                                                       |
| djangocms               | 32.6 us                                                                | 31.9 us: 1.02x faster                                                       |
| pprint_safe_repr        | 682 ms                                                                 | 670 ms: 1.02x faster                                                        |
| pprint_pformat          | 1.39 sec                                                               | 1.37 sec: 1.02x faster                                                      |
| pycparser               | 1.10 sec                                                               | 1.08 sec: 1.02x faster                                                      |
| nqueens                 | 78.4 ms                                                                | 77.2 ms: 1.02x faster                                                       |
| python_startup_no_site  | 6.49 ms                                                                | 6.39 ms: 1.02x faster                                                       |
| python_startup          | 8.98 ms                                                                | 8.85 ms: 1.01x faster                                                       |
| go                      | 135 ms                                                                 | 134 ms: 1.01x faster                                                        |
| json_dumps              | 9.45 ms                                                                | 9.32 ms: 1.01x faster                                                       |
| django_template         | 32.7 ms                                                                | 32.3 ms: 1.01x faster                                                       |
| xml_etree_iterparse     | 104 ms                                                                 | 102 ms: 1.01x faster                                                        |
| meteor_contest          | 104 ms                                                                 | 103 ms: 1.01x faster                                                        |
| scimark_fft             | 305 ms                                                                 | 301 ms: 1.01x faster                                                        |
| pickle_pure_python      | 283 us                                                                 | 280 us: 1.01x faster                                                        |
| xml_etree_parse         | 149 ms                                                                 | 148 ms: 1.01x faster                                                        |
| create_gc_cycles        | 1.47 ms                                                                | 1.46 ms: 1.01x faster                                                       |
| scimark_lu              | 106 ms                                                                 | 106 ms: 1.01x faster                                                        |
| hexiom                  | 6.01 ms                                                                | 5.96 ms: 1.01x faster                                                       |
| bench_thread_pool       | 785 us                                                                 | 779 us: 1.01x faster                                                        |
| 2to3                    | 251 ms                                                                 | 249 ms: 1.01x faster                                                        |
| scimark_sor             | 106 ms                                                                 | 105 ms: 1.01x faster                                                        |
| pathlib                 | 17.8 ms                                                                | 17.7 ms: 1.01x faster                                                       |
| deepcopy                | 327 us                                                                 | 325 us: 1.01x faster                                                        |
| coverage                | 96.6 ms                                                                | 96.1 ms: 1.01x faster                                                       |
| async_generators        | 351 ms                                                                 | 349 ms: 1.00x faster                                                        |
| aiohttp                 | 996 us                                                                 | 991 us: 1.00x faster                                                        |
| docutils                | 2.49 sec                                                               | 2.48 sec: 1.00x faster                                                      |
| asyncio_tcp             | 499 ms                                                                 | 497 ms: 1.00x faster                                                        |
| sympy_integrate         | 19.6 ms                                                                | 19.7 ms: 1.00x slower                                                       |
| sqlglot_transpile       | 1.69 ms                                                                | 1.70 ms: 1.00x slower                                                       |
| sqlglot_parse           | 1.40 ms                                                                | 1.41 ms: 1.00x slower                                                       |
| sympy_str               | 269 ms                                                                 | 270 ms: 1.01x slower                                                        |
| genshi_xml              | 45.8 ms                                                                | 46.0 ms: 1.01x slower                                                       |
| dulwich_log             | 62.6 ms                                                                | 62.9 ms: 1.01x slower                                                       |
| scimark_monte_carlo     | 65.5 ms                                                                | 65.9 ms: 1.01x slower                                                       |
| regex_dna               | 205 ms                                                                 | 207 ms: 1.01x slower                                                        |
| regex_effbot            | 3.48 ms                                                                | 3.51 ms: 1.01x slower                                                       |
| sqlite_synth            | 2.57 us                                                                | 2.59 us: 1.01x slower                                                       |
| sqlglot_optimize        | 50.9 ms                                                                | 51.4 ms: 1.01x slower                                                       |
| pickle_dict             | 31.2 us                                                                | 31.6 us: 1.01x slower                                                       |
| sqlglot_normalize       | 105 ms                                                                 | 106 ms: 1.01x slower                                                        |
| raytrace                | 279 ms                                                                 | 283 ms: 1.02x slower                                                        |
| xml_etree_process       | 53.2 ms                                                                | 54.1 ms: 1.02x slower                                                       |
| deepcopy_memo           | 33.8 us                                                                | 34.4 us: 1.02x slower                                                       |
| crypto_pyaes            | 72.8 ms                                                                | 74.1 ms: 1.02x slower                                                       |
| xml_etree_generate      | 77.0 ms                                                                | 78.5 ms: 1.02x slower                                                       |
| richards                | 41.2 ms                                                                | 42.2 ms: 1.02x slower                                                       |
| coroutines              | 25.4 ms                                                                | 26.0 ms: 1.02x slower                                                       |
| spectral_norm           | 95.0 ms                                                                | 97.4 ms: 1.03x slower                                                       |
| pickle_list             | 4.02 us                                                                | 4.21 us: 1.05x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (28): html5lib, dask, fannkuch, gunicorn, regex_compile, unpickle_pure_python, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, deepcopy_reduce, thrift, bench_mp_pool, unpickle_list, mako, tornado_http, async_tree_io, float, pickle, nbody, sympy_sum, deltablue, unpickle, mypy, chameleon, pyflate, sympy_expand, json_loads, json
