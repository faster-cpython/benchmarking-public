
# Results vs. base

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 7ffdaa2
- commit date: 2023-01-18
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 250 ms: 1.01x faster                                                        |
| chameleon      | 6.49 ms                                                                | 6.28 ms: 1.03x faster                                                       |
| docutils       | 2.49 sec                                                               | 2.52 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 95.7 ms                                                                | 93.9 ms: 1.02x faster                                                       |
| pidigits       | 197 ms                                                                 | 198 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.64 ms                                                                | 3.44 ms: 1.06x faster                                                       |
| regex_v8       | 22.4 ms                                                                | 21.8 ms: 1.03x faster                                                       |
| regex_dna      | 210 ms                                                                 | 208 ms: 1.01x faster                                                        |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python  | 285 us                                                                 | 280 us: 1.01x faster                                                        |
| xml_etree_generate  | 77.7 ms                                                                | 77.9 ms: 1.00x slower                                                       |
| unpickle            | 13.1 us                                                                | 13.3 us: 1.01x slower                                                       |
| pickle              | 9.95 us                                                                | 10.1 us: 1.01x slower                                                       |
| xml_etree_iterparse | 103 ms                                                                 | 105 ms: 1.02x slower                                                        |
| pickle_dict         | 30.3 us                                                                | 31.0 us: 1.02x slower                                                       |
| unpickle_list       | 4.98 us                                                                | 5.11 us: 1.03x slower                                                       |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (6): xml_etree_parse, json_loads, unpickle_pure_python, pickle_list, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.45 ms                                                                | 6.39 ms: 1.01x faster                                                       |
| python_startup         | 8.90 ms                                                                | 8.84 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 33.4 ms                                                                | 32.5 ms: 1.03x faster                                                       |
| genshi_text     | 20.8 ms                                                                | 20.3 ms: 1.02x faster                                                       |
| genshi_xml      | 46.8 ms                                                                | 46.6 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal            | 4.03 ms                                                                | 3.81 ms: 1.06x faster                                                       |
| regex_effbot            | 3.64 ms                                                                | 3.44 ms: 1.06x faster                                                       |
| generators              | 78.1 ms                                                                | 75.0 ms: 1.04x faster                                                       |
| scimark_fft             | 306 ms                                                                 | 296 ms: 1.03x faster                                                        |
| logging_silent          | 95.3 ns                                                                | 92.1 ns: 1.03x faster                                                       |
| chameleon               | 6.49 ms                                                                | 6.28 ms: 1.03x faster                                                       |
| pyflate                 | 403 ms                                                                 | 391 ms: 1.03x faster                                                        |
| meteor_contest          | 106 ms                                                                 | 103 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult | 4.06 ms                                                                | 3.93 ms: 1.03x faster                                                       |
| pycparser               | 1.15 sec                                                               | 1.12 sec: 1.03x faster                                                      |
| regex_v8                | 22.4 ms                                                                | 21.8 ms: 1.03x faster                                                       |
| django_template         | 33.4 ms                                                                | 32.5 ms: 1.03x faster                                                       |
| spectral_norm           | 96.7 ms                                                                | 94.4 ms: 1.02x faster                                                       |
| genshi_text             | 20.8 ms                                                                | 20.3 ms: 1.02x faster                                                       |
| go                      | 136 ms                                                                 | 134 ms: 1.02x faster                                                        |
| coroutines              | 25.1 ms                                                                | 24.6 ms: 1.02x faster                                                       |
| nbody                   | 95.7 ms                                                                | 93.9 ms: 1.02x faster                                                       |
| scimark_sor             | 106 ms                                                                 | 104 ms: 1.02x faster                                                        |
| pickle_pure_python      | 285 us                                                                 | 280 us: 1.01x faster                                                        |
| dask                    | 499 ms                                                                 | 492 ms: 1.01x faster                                                        |
| json                    | 4.64 ms                                                                | 4.58 ms: 1.01x faster                                                       |
| raytrace                | 283 ms                                                                 | 280 ms: 1.01x faster                                                        |
| chaos                   | 65.1 ms                                                                | 64.4 ms: 1.01x faster                                                       |
| richards                | 42.6 ms                                                                | 42.1 ms: 1.01x faster                                                       |
| regex_dna               | 210 ms                                                                 | 208 ms: 1.01x faster                                                        |
| pathlib                 | 17.7 ms                                                                | 17.5 ms: 1.01x faster                                                       |
| scimark_monte_carlo     | 66.7 ms                                                                | 66.0 ms: 1.01x faster                                                       |
| sympy_expand            | 456 ms                                                                 | 452 ms: 1.01x faster                                                        |
| 2to3                    | 252 ms                                                                 | 250 ms: 1.01x faster                                                        |
| python_startup_no_site  | 6.45 ms                                                                | 6.39 ms: 1.01x faster                                                       |
| sympy_str               | 271 ms                                                                 | 269 ms: 1.01x faster                                                        |
| asyncio_tcp             | 493 ms                                                                 | 489 ms: 1.01x faster                                                        |
| create_gc_cycles        | 1.45 ms                                                                | 1.44 ms: 1.01x faster                                                       |
| python_startup          | 8.90 ms                                                                | 8.84 ms: 1.01x faster                                                       |
| nqueens                 | 76.8 ms                                                                | 76.3 ms: 1.01x faster                                                       |
| pprint_pformat          | 1.42 sec                                                               | 1.41 sec: 1.01x faster                                                      |
| coverage                | 95.9 ms                                                                | 95.3 ms: 1.01x faster                                                       |
| genshi_xml              | 46.8 ms                                                                | 46.6 ms: 1.01x faster                                                       |
| pidigits                | 197 ms                                                                 | 198 ms: 1.00x slower                                                        |
| async_generators        | 350 ms                                                                 | 351 ms: 1.00x slower                                                        |
| xml_etree_generate      | 77.7 ms                                                                | 77.9 ms: 1.00x slower                                                       |
| regex_compile           | 128 ms                                                                 | 128 ms: 1.00x slower                                                        |
| sqlglot_optimize        | 50.8 ms                                                                | 51.0 ms: 1.00x slower                                                       |
| sqlglot_parse           | 1.40 ms                                                                | 1.40 ms: 1.00x slower                                                       |
| bench_thread_pool       | 775 us                                                                 | 780 us: 1.01x slower                                                        |
| sqlite_synth            | 2.56 us                                                                | 2.57 us: 1.01x slower                                                       |
| logging_simple          | 5.72 us                                                                | 5.77 us: 1.01x slower                                                       |
| pprint_safe_repr        | 689 ms                                                                 | 696 ms: 1.01x slower                                                        |
| scimark_lu              | 106 ms                                                                 | 107 ms: 1.01x slower                                                        |
| docutils                | 2.49 sec                                                               | 2.52 sec: 1.01x slower                                                      |
| deepcopy                | 328 us                                                                 | 332 us: 1.01x slower                                                        |
| unpickle                | 13.1 us                                                                | 13.3 us: 1.01x slower                                                       |
| pickle                  | 9.95 us                                                                | 10.1 us: 1.01x slower                                                       |
| deepcopy_memo           | 34.0 us                                                                | 34.5 us: 1.01x slower                                                       |
| thrift                  | 736 us                                                                 | 747 us: 1.01x slower                                                        |
| xml_etree_iterparse     | 103 ms                                                                 | 105 ms: 1.02x slower                                                        |
| pickle_dict             | 30.3 us                                                                | 31.0 us: 1.02x slower                                                       |
| deepcopy_reduce         | 2.90 us                                                                | 2.96 us: 1.02x slower                                                       |
| unpickle_list           | 4.98 us                                                                | 5.11 us: 1.03x slower                                                       |
| deltablue               | 3.19 ms                                                                | 3.28 ms: 1.03x slower                                                       |
| fannkuch                | 358 ms                                                                 | 371 ms: 1.04x slower                                                        |
| unpack_sequence         | 42.3 ns                                                                | 44.3 ns: 1.05x slower                                                       |
| mdp                     | 2.52 sec                                                               | 2.66 sec: 1.05x slower                                                      |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (28): async_tree_memoization, xml_etree_parse, html5lib, json_loads, async_tree_cpu_io_mixed, async_tree_none, unpickle_pure_python, dulwich_log, crypto_pyaes, aiohttp, mako, sympy_integrate, bench_mp_pool, hexiom, telco, sqlglot_transpile, float, gunicorn, pickle_list, tornado_http, sqlglot_normalize, sympy_sum, mypy, json_dumps, logging_format, xml_etree_process, async_tree_io, djangocms
