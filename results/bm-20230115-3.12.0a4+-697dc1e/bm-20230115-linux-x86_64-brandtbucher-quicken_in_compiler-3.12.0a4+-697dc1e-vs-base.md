
# Results vs. base

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 697dc1e
- commit date: 2023-01-15
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 251 ms: 1.01x faster                                                        |
| chameleon      | 6.42 ms                                                                | 6.35 ms: 1.01x faster                                                       |
| docutils       | 2.52 sec                                                               | 2.48 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                 | 189 ms: 1.04x faster                                                        |
| float          | 72.6 ms                                                                | 71.5 ms: 1.01x faster                                                       |
| nbody          | 93.8 ms                                                                | 94.8 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 128 ms: 1.01x faster                                                        |
| regex_effbot   | 3.44 ms                                                                | 3.51 ms: 1.02x slower                                                       |
| regex_v8       | 21.0 ms                                                                | 21.7 ms: 1.03x slower                                                       |
| regex_dna      | 201 ms                                                                 | 211 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.2 us                                                                | 29.9 us: 1.08x faster                                                       |
| pickle_list          | 4.26 us                                                                | 4.06 us: 1.05x faster                                                       |
| pickle_pure_python   | 284 us                                                                 | 279 us: 1.02x faster                                                        |
| pickle               | 10.3 us                                                                | 10.2 us: 1.02x faster                                                       |
| json_loads           | 24.3 us                                                                | 23.9 us: 1.02x faster                                                       |
| unpickle_list        | 5.08 us                                                                | 5.01 us: 1.01x faster                                                       |
| xml_etree_process    | 54.4 ms                                                                | 54.1 ms: 1.01x faster                                                       |
| unpickle_pure_python | 197 us                                                                 | 196 us: 1.01x faster                                                        |
| xml_etree_generate   | 79.1 ms                                                                | 78.8 ms: 1.00x faster                                                       |
| xml_etree_iterparse  | 106 ms                                                                 | 109 ms: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (3): unpickle, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.49 ms                                                                | 6.22 ms: 1.04x faster                                                       |
| python_startup         | 8.96 ms                                                                | 8.68 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.04x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 22.1 ms                                                                | 20.1 ms: 1.10x faster                                                       |
| django_template | 32.9 ms                                                                | 32.0 ms: 1.03x faster                                                       |
| genshi_xml      | 46.8 ms                                                                | 46.1 ms: 1.02x faster                                                       |
| mako            | 9.66 ms                                                                | 9.63 ms: 1.00x faster                                                       |
| Geometric mean  | (ref)                                                                  | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text             | 22.1 ms                                                                | 20.1 ms: 1.10x faster                                                       |
| pickle_dict             | 32.2 us                                                                | 29.9 us: 1.08x faster                                                       |
| pickle_list             | 4.26 us                                                                | 4.06 us: 1.05x faster                                                       |
| python_startup_no_site  | 6.49 ms                                                                | 6.22 ms: 1.04x faster                                                       |
| pidigits                | 197 ms                                                                 | 189 ms: 1.04x faster                                                        |
| gc_traversal            | 3.96 ms                                                                | 3.81 ms: 1.04x faster                                                       |
| go                      | 136 ms                                                                 | 131 ms: 1.03x faster                                                        |
| python_startup          | 8.96 ms                                                                | 8.68 ms: 1.03x faster                                                       |
| django_template         | 32.9 ms                                                                | 32.0 ms: 1.03x faster                                                       |
| deepcopy_reduce         | 2.97 us                                                                | 2.89 us: 1.03x faster                                                       |
| coroutines              | 25.6 ms                                                                | 24.9 ms: 1.03x faster                                                       |
| create_gc_cycles        | 1.48 ms                                                                | 1.45 ms: 1.03x faster                                                       |
| richards                | 42.9 ms                                                                | 42.0 ms: 1.02x faster                                                       |
| sqlglot_optimize        | 51.3 ms                                                                | 50.2 ms: 1.02x faster                                                       |
| pickle_pure_python      | 284 us                                                                 | 279 us: 1.02x faster                                                        |
| telco                   | 6.38 ms                                                                | 6.26 ms: 1.02x faster                                                       |
| pickle                  | 10.3 us                                                                | 10.2 us: 1.02x faster                                                       |
| json_loads              | 24.3 us                                                                | 23.9 us: 1.02x faster                                                       |
| spectral_norm           | 97.7 ms                                                                | 96.0 ms: 1.02x faster                                                       |
| genshi_xml              | 46.8 ms                                                                | 46.1 ms: 1.02x faster                                                       |
| logging_simple          | 5.74 us                                                                | 5.65 us: 1.02x faster                                                       |
| pathlib                 | 17.9 ms                                                                | 17.6 ms: 1.02x faster                                                       |
| float                   | 72.6 ms                                                                | 71.5 ms: 1.01x faster                                                       |
| deltablue               | 3.23 ms                                                                | 3.19 ms: 1.01x faster                                                       |
| unpickle_list           | 5.08 us                                                                | 5.01 us: 1.01x faster                                                       |
| sqlglot_transpile       | 1.71 ms                                                                | 1.68 ms: 1.01x faster                                                       |
| coverage                | 97.3 ms                                                                | 96.0 ms: 1.01x faster                                                       |
| logging_format          | 6.34 us                                                                | 6.26 us: 1.01x faster                                                       |
| docutils                | 2.52 sec                                                               | 2.48 sec: 1.01x faster                                                      |
| sqlglot_normalize       | 105 ms                                                                 | 103 ms: 1.01x faster                                                        |
| chameleon               | 6.42 ms                                                                | 6.35 ms: 1.01x faster                                                       |
| asyncio_tcp             | 490 ms                                                                 | 485 ms: 1.01x faster                                                        |
| deepcopy                | 327 us                                                                 | 324 us: 1.01x faster                                                        |
| async_generators        | 351 ms                                                                 | 348 ms: 1.01x faster                                                        |
| sqlglot_parse           | 1.41 ms                                                                | 1.40 ms: 1.01x faster                                                       |
| 2to3                    | 253 ms                                                                 | 251 ms: 1.01x faster                                                        |
| sympy_expand            | 456 ms                                                                 | 452 ms: 1.01x faster                                                        |
| regex_compile           | 129 ms                                                                 | 128 ms: 1.01x faster                                                        |
| async_tree_io           | 1.33 sec                                                               | 1.32 sec: 1.01x faster                                                      |
| sympy_sum               | 164 ms                                                                 | 162 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 674 ms                                                                 | 670 ms: 1.01x faster                                                        |
| thrift                  | 746 us                                                                 | 742 us: 1.01x faster                                                        |
| xml_etree_process       | 54.4 ms                                                                | 54.1 ms: 1.01x faster                                                       |
| unpickle_pure_python    | 197 us                                                                 | 196 us: 1.01x faster                                                        |
| sympy_integrate         | 20.2 ms                                                                | 20.2 ms: 1.00x faster                                                       |
| mako                    | 9.66 ms                                                                | 9.63 ms: 1.00x faster                                                       |
| xml_etree_generate      | 79.1 ms                                                                | 78.8 ms: 1.00x faster                                                       |
| aiohttp                 | 994 us                                                                 | 999 us: 1.01x slower                                                        |
| scimark_fft             | 306 ms                                                                 | 308 ms: 1.01x slower                                                        |
| gunicorn                | 1.07 ms                                                                | 1.08 ms: 1.01x slower                                                       |
| pyflate                 | 400 ms                                                                 | 404 ms: 1.01x slower                                                        |
| raytrace                | 280 ms                                                                 | 283 ms: 1.01x slower                                                        |
| nbody                   | 93.8 ms                                                                | 94.8 ms: 1.01x slower                                                       |
| hexiom                  | 5.95 ms                                                                | 6.03 ms: 1.01x slower                                                       |
| pycparser               | 1.10 sec                                                               | 1.11 sec: 1.01x slower                                                      |
| scimark_lu              | 107 ms                                                                 | 109 ms: 1.01x slower                                                        |
| generators              | 74.7 ms                                                                | 75.9 ms: 1.02x slower                                                       |
| mdp                     | 2.43 sec                                                               | 2.47 sec: 1.02x slower                                                      |
| scimark_monte_carlo     | 65.2 ms                                                                | 66.4 ms: 1.02x slower                                                       |
| regex_effbot            | 3.44 ms                                                                | 3.51 ms: 1.02x slower                                                       |
| xml_etree_iterparse     | 106 ms                                                                 | 109 ms: 1.03x slower                                                        |
| djangocms               | 31.6 us                                                                | 32.5 us: 1.03x slower                                                       |
| chaos                   | 63.6 ms                                                                | 65.5 ms: 1.03x slower                                                       |
| nqueens                 | 76.2 ms                                                                | 78.5 ms: 1.03x slower                                                       |
| regex_v8                | 21.0 ms                                                                | 21.7 ms: 1.03x slower                                                       |
| regex_dna               | 201 ms                                                                 | 211 ms: 1.05x slower                                                        |
| unpack_sequence         | 41.6 ns                                                                | 44.9 ns: 1.08x slower                                                       |
| scimark_sparse_mat_mult | 4.06 ms                                                                | 4.47 ms: 1.10x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (23): unpickle, async_tree_memoization, async_tree_none, deepcopy_memo, async_tree_cpu_io_mixed, meteor_contest, dask, json_dumps, json, fannkuch, mypy, pprint_pformat, bench_thread_pool, crypto_pyaes, bench_mp_pool, tornado_http, sqlite_synth, sympy_str, html5lib, dulwich_log, scimark_sor, xml_etree_parse, logging_silent
