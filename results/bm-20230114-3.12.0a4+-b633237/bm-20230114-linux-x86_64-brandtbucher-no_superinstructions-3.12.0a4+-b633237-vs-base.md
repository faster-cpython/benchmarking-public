
# Results vs. base

- fork: brandtbucher
- ref: no_superinstructions
- machine: linux-x86_64
- commit hash: b633237
- commit date: 2023-01-14
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230119-linux-x86_64-python-8a2d4f4e8eea86352de3-3.12.0a4+-8a2d4f4 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 255 ms: 1.02x slower                                                         |
| chameleon      | 6.23 ms                                                                | 6.49 ms: 1.04x slower                                                        |
| docutils       | 2.49 sec                                                               | 2.50 sec: 1.00x slower                                                       |
| html5lib       | 59.5 ms                                                                | 60.6 ms: 1.02x slower                                                        |
| tornado_http   | 93.3 ms                                                                | 94.9 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230119-linux-x86_64-python-8a2d4f4e8eea86352de3-3.12.0a4+-8a2d4f4 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 190 ms                                                                 | 193 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230119-linux-x86_64-python-8a2d4f4e8eea86352de3-3.12.0a4+-8a2d4f4 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 22.3 ms                                                                | 21.2 ms: 1.05x faster                                                        |
| regex_dna      | 210 ms                                                                 | 207 ms: 1.01x faster                                                         |
| regex_compile  | 130 ms                                                                 | 133 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230119-linux-x86_64-python-8a2d4f4e8eea86352de3-3.12.0a4+-8a2d4f4 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 31.0 us                                                                | 29.5 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 108 ms                                                                 | 105 ms: 1.03x faster                                                         |
| xml_etree_generate   | 77.7 ms                                                                | 77.0 ms: 1.01x faster                                                        |
| unpickle_list        | 4.94 us                                                                | 4.91 us: 1.01x faster                                                        |
| pickle               | 9.96 us                                                                | 10.0 us: 1.01x slower                                                        |
| unpickle_pure_python | 198 us                                                                 | 201 us: 1.01x slower                                                         |
| pickle_pure_python   | 279 us                                                                 | 287 us: 1.03x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (6): unpickle, xml_etree_process, json_loads, xml_etree_parse, json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230119-linux-x86_64-python-8a2d4f4e8eea86352de3-3.12.0a4+-8a2d4f4 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.40 ms                                                                | 6.30 ms: 1.02x faster                                                        |
| python_startup         | 8.84 ms                                                                | 8.74 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230119-linux-x86_64-python-8a2d4f4e8eea86352de3-3.12.0a4+-8a2d4f4 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 46.5 ms                                                                | 47.1 ms: 1.01x slower                                                        |
| django_template | 32.2 ms                                                                | 32.7 ms: 1.02x slower                                                        |
| mako            | 9.43 ms                                                                | 9.89 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230119-linux-x86_64-python-8a2d4f4e8eea86352de3-3.12.0a4+-8a2d4f4 | bm-20230114-linux-x86_64-brandtbucher-no_superinstructions-3.12.0a4+-b633237 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal            | 4.16 ms                                                                | 3.50 ms: 1.19x faster                                                        |
| regex_v8                | 22.3 ms                                                                | 21.2 ms: 1.05x faster                                                        |
| pickle_dict             | 31.0 us                                                                | 29.5 us: 1.05x faster                                                        |
| generators              | 77.8 ms                                                                | 74.6 ms: 1.04x faster                                                        |
| pycparser               | 1.14 sec                                                               | 1.11 sec: 1.03x faster                                                       |
| xml_etree_iterparse     | 108 ms                                                                 | 105 ms: 1.03x faster                                                         |
| python_startup_no_site  | 6.40 ms                                                                | 6.30 ms: 1.02x faster                                                        |
| coverage                | 97.7 ms                                                                | 96.2 ms: 1.02x faster                                                        |
| regex_dna               | 210 ms                                                                 | 207 ms: 1.01x faster                                                         |
| python_startup          | 8.84 ms                                                                | 8.74 ms: 1.01x faster                                                        |
| fannkuch                | 378 ms                                                                 | 374 ms: 1.01x faster                                                         |
| scimark_lu              | 108 ms                                                                 | 106 ms: 1.01x faster                                                         |
| telco                   | 6.49 ms                                                                | 6.43 ms: 1.01x faster                                                        |
| xml_etree_generate      | 77.7 ms                                                                | 77.0 ms: 1.01x faster                                                        |
| sqlite_synth            | 2.60 us                                                                | 2.58 us: 1.01x faster                                                        |
| pyflate                 | 401 ms                                                                 | 398 ms: 1.01x faster                                                         |
| unpickle_list           | 4.94 us                                                                | 4.91 us: 1.01x faster                                                        |
| docutils                | 2.49 sec                                                               | 2.50 sec: 1.00x slower                                                       |
| sympy_sum               | 164 ms                                                                 | 165 ms: 1.01x slower                                                         |
| async_generators        | 354 ms                                                                 | 356 ms: 1.01x slower                                                         |
| coroutines              | 24.9 ms                                                                | 25.0 ms: 1.01x slower                                                        |
| bench_thread_pool       | 779 us                                                                 | 784 us: 1.01x slower                                                         |
| sqlglot_optimize        | 51.1 ms                                                                | 51.4 ms: 1.01x slower                                                        |
| sqlglot_parse           | 1.39 ms                                                                | 1.40 ms: 1.01x slower                                                        |
| sympy_integrate         | 20.4 ms                                                                | 20.5 ms: 1.01x slower                                                        |
| pickle                  | 9.96 us                                                                | 10.0 us: 1.01x slower                                                        |
| pprint_safe_repr        | 670 ms                                                                 | 676 ms: 1.01x slower                                                         |
| logging_silent          | 90.8 ns                                                                | 91.7 ns: 1.01x slower                                                        |
| deepcopy_reduce         | 2.92 us                                                                | 2.95 us: 1.01x slower                                                        |
| sqlglot_transpile       | 1.68 ms                                                                | 1.70 ms: 1.01x slower                                                        |
| aiohttp                 | 992 us                                                                 | 1.00 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 739 ms                                                                 | 749 ms: 1.01x slower                                                         |
| genshi_xml              | 46.5 ms                                                                | 47.1 ms: 1.01x slower                                                        |
| deltablue               | 3.18 ms                                                                | 3.23 ms: 1.01x slower                                                        |
| unpickle_pure_python    | 198 us                                                                 | 201 us: 1.01x slower                                                         |
| sympy_expand            | 459 ms                                                                 | 466 ms: 1.01x slower                                                         |
| 2to3                    | 252 ms                                                                 | 255 ms: 1.02x slower                                                         |
| tornado_http            | 93.3 ms                                                                | 94.9 ms: 1.02x slower                                                        |
| sympy_str               | 283 ms                                                                 | 288 ms: 1.02x slower                                                         |
| scimark_sor             | 105 ms                                                                 | 107 ms: 1.02x slower                                                         |
| pidigits                | 190 ms                                                                 | 193 ms: 1.02x slower                                                         |
| gunicorn                | 1.06 ms                                                                | 1.08 ms: 1.02x slower                                                        |
| django_template         | 32.2 ms                                                                | 32.7 ms: 1.02x slower                                                        |
| dulwich_log             | 61.2 ms                                                                | 62.4 ms: 1.02x slower                                                        |
| raytrace                | 283 ms                                                                 | 288 ms: 1.02x slower                                                         |
| html5lib                | 59.5 ms                                                                | 60.6 ms: 1.02x slower                                                        |
| go                      | 134 ms                                                                 | 137 ms: 1.02x slower                                                         |
| regex_compile           | 130 ms                                                                 | 133 ms: 1.02x slower                                                         |
| dask                    | 496 ms                                                                 | 507 ms: 1.02x slower                                                         |
| crypto_pyaes            | 76.0 ms                                                                | 77.7 ms: 1.02x slower                                                        |
| hexiom                  | 6.03 ms                                                                | 6.18 ms: 1.02x slower                                                        |
| chaos                   | 68.6 ms                                                                | 70.4 ms: 1.03x slower                                                        |
| djangocms               | 32.0 us                                                                | 32.9 us: 1.03x slower                                                        |
| scimark_fft             | 308 ms                                                                 | 317 ms: 1.03x slower                                                         |
| pickle_pure_python      | 279 us                                                                 | 287 us: 1.03x slower                                                         |
| pathlib                 | 17.7 ms                                                                | 18.2 ms: 1.03x slower                                                        |
| deepcopy                | 327 us                                                                 | 336 us: 1.03x slower                                                         |
| logging_simple          | 5.61 us                                                                | 5.82 us: 1.04x slower                                                        |
| chameleon               | 6.23 ms                                                                | 6.49 ms: 1.04x slower                                                        |
| richards                | 42.0 ms                                                                | 44.0 ms: 1.05x slower                                                        |
| mako                    | 9.43 ms                                                                | 9.89 ms: 1.05x slower                                                        |
| logging_format          | 6.19 us                                                                | 6.52 us: 1.05x slower                                                        |
| mdp                     | 2.45 sec                                                               | 2.61 sec: 1.06x slower                                                       |
| deepcopy_memo           | 33.7 us                                                                | 36.1 us: 1.07x slower                                                        |
| unpack_sequence         | 41.6 ns                                                                | 49.0 ns: 1.18x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (26): async_tree_memoization, unpickle, thrift, nqueens, xml_etree_process, scimark_sparse_mat_mult, json_loads, pprint_pformat, regex_effbot, bench_mp_pool, sqlglot_normalize, float, genshi_text, nbody, xml_etree_parse, asyncio_tcp, create_gc_cycles, async_tree_io, json_dumps, pickle_list, scimark_monte_carlo, meteor_contest, json, spectral_norm, async_tree_none, mypy
