# Results vs. base

- fork: gpshead
- ref: traceback_timestamps
- machine: linux-x86_64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.002x slower
- HPT reliability: 65.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.59 sec                                                              | 2.58 sec: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 508 ms                                                                | 490 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 499 ms                                                                | 484 ms: 1.03x faster                                                   |
| async_tree_memoization     | 317 ms                                                                | 312 ms: 1.02x faster                                                   |
| async_tree_none            | 264 ms                                                                | 260 ms: 1.01x faster                                                   |
| async_tree_none_tg         | 252 ms                                                                | 250 ms: 1.01x faster                                                   |
| async_generators           | 409 ms                                                                | 413 ms: 1.01x slower                                                   |
| coroutines                 | 25.0 ms                                                               | 26.4 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (4): async_tree_io, async_tree_memoization_tg, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 192 ms                                                                | 188 ms: 1.02x faster                                                   |
| float          | 71.5 ms                                                               | 72.9 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                | 128 ms: 1.00x slower                                                   |
| regex_dna      | 210 ms                                                                | 211 ms: 1.01x slower                                                   |
| regex_effbot   | 3.25 ms                                                               | 3.31 ms: 1.02x slower                                                  |
| regex_v8       | 23.3 ms                                                               | 23.9 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.06 sec                                                              | 2.03 sec: 1.01x faster                                                 |
| xml_etree_iterparse  | 99.7 ms                                                               | 98.8 ms: 1.01x faster                                                  |
| json_loads           | 28.5 us                                                               | 28.8 us: 1.01x slower                                                  |
| unpickle_pure_python | 219 us                                                                | 223 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_process, xml_etree_generate, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.1 ms: 1.00x faster                                                  |
| python_startup_no_site | 6.90 ms                                                               | 6.89 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 32.3 ms                                                               | 32.6 ms: 1.01x slower                                                  |
| mako            | 11.3 ms                                                               | 11.7 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pathlib                    | 17.5 ms                                                               | 16.7 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed    | 508 ms                                                                | 490 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 499 ms                                                                | 484 ms: 1.03x faster                                                   |
| pidigits                   | 192 ms                                                                | 188 ms: 1.02x faster                                                   |
| comprehensions             | 16.3 us                                                               | 15.9 us: 1.02x faster                                                  |
| async_tree_memoization     | 317 ms                                                                | 312 ms: 1.02x faster                                                   |
| sqlite_synth               | 2.86 us                                                               | 2.81 us: 1.02x faster                                                  |
| deepcopy_reduce            | 2.71 us                                                               | 2.68 us: 1.01x faster                                                  |
| async_tree_none            | 264 ms                                                                | 260 ms: 1.01x faster                                                   |
| tomli_loads                | 2.06 sec                                                              | 2.03 sec: 1.01x faster                                                 |
| subparsers                 | 23.7 ms                                                               | 23.4 ms: 1.01x faster                                                  |
| dulwich_log                | 60.1 ms                                                               | 59.5 ms: 1.01x faster                                                  |
| async_tree_none_tg         | 252 ms                                                                | 250 ms: 1.01x faster                                                   |
| sympy_expand               | 457 ms                                                                | 453 ms: 1.01x faster                                                   |
| many_optionals             | 967 us                                                                | 958 us: 1.01x faster                                                   |
| telco                      | 8.15 ms                                                               | 8.08 ms: 1.01x faster                                                  |
| xml_etree_iterparse        | 99.7 ms                                                               | 98.8 ms: 1.01x faster                                                  |
| fannkuch                   | 421 ms                                                                | 418 ms: 1.01x faster                                                   |
| logging_silent             | 477 ns                                                                | 474 ns: 1.01x faster                                                   |
| deltablue                  | 3.55 ms                                                               | 3.53 ms: 1.01x faster                                                  |
| sympy_str                  | 269 ms                                                                | 267 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 4.57 sec                                                              | 4.55 sec: 1.00x faster                                                 |
| nqueens                    | 81.7 ms                                                               | 81.3 ms: 1.00x faster                                                  |
| python_startup             | 12.2 ms                                                               | 12.1 ms: 1.00x faster                                                  |
| create_gc_cycles           | 2.56 ms                                                               | 2.55 ms: 1.00x faster                                                  |
| docutils                   | 2.59 sec                                                              | 2.58 sec: 1.00x faster                                                 |
| python_startup_no_site     | 6.90 ms                                                               | 6.89 ms: 1.00x faster                                                  |
| pyflate                    | 427 ms                                                                | 429 ms: 1.00x slower                                                   |
| regex_compile              | 127 ms                                                                | 128 ms: 1.00x slower                                                   |
| hexiom                     | 6.05 ms                                                               | 6.08 ms: 1.00x slower                                                  |
| mdp                        | 1.22 sec                                                              | 1.23 sec: 1.00x slower                                                 |
| crypto_pyaes               | 75.2 ms                                                               | 75.5 ms: 1.00x slower                                                  |
| richards_super             | 49.2 ms                                                               | 49.4 ms: 1.00x slower                                                  |
| chaos                      | 61.3 ms                                                               | 61.6 ms: 1.00x slower                                                  |
| sqlglot_v2_optimize        | 52.5 ms                                                               | 52.7 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 786 ms                                                                | 792 ms: 1.01x slower                                                   |
| deepcopy_memo              | 29.2 us                                                               | 29.4 us: 1.01x slower                                                  |
| sqlglot_v2_parse           | 1.26 ms                                                               | 1.27 ms: 1.01x slower                                                  |
| regex_dna                  | 210 ms                                                                | 211 ms: 1.01x slower                                                   |
| django_template            | 32.3 ms                                                               | 32.6 ms: 1.01x slower                                                  |
| generators                 | 29.8 ms                                                               | 30.1 ms: 1.01x slower                                                  |
| sqlglot_v2_transpile       | 1.57 ms                                                               | 1.58 ms: 1.01x slower                                                  |
| async_generators           | 409 ms                                                                | 413 ms: 1.01x slower                                                   |
| json_loads                 | 28.5 us                                                               | 28.8 us: 1.01x slower                                                  |
| meteor_contest             | 106 ms                                                                | 107 ms: 1.01x slower                                                   |
| spectral_norm              | 109 ms                                                                | 110 ms: 1.01x slower                                                   |
| scimark_sor                | 121 ms                                                                | 123 ms: 1.01x slower                                                   |
| scimark_fft                | 379 ms                                                                | 384 ms: 1.01x slower                                                   |
| go                         | 111 ms                                                                | 112 ms: 1.01x slower                                                   |
| unpickle_pure_python       | 219 us                                                                | 223 us: 1.02x slower                                                   |
| typing_runtime_protocols   | 167 us                                                                | 170 us: 1.02x slower                                                   |
| gc_traversal               | 4.75 ms                                                               | 4.84 ms: 1.02x slower                                                  |
| regex_effbot               | 3.25 ms                                                               | 3.31 ms: 1.02x slower                                                  |
| raytrace                   | 270 ms                                                                | 276 ms: 1.02x slower                                                   |
| float                      | 71.5 ms                                                               | 72.9 ms: 1.02x slower                                                  |
| scimark_monte_carlo        | 67.2 ms                                                               | 68.6 ms: 1.02x slower                                                  |
| regex_v8                   | 23.3 ms                                                               | 23.9 ms: 1.03x slower                                                  |
| mako                       | 11.3 ms                                                               | 11.7 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 5.02 ms                                                               | 5.20 ms: 1.03x slower                                                  |
| coroutines                 | 25.0 ms                                                               | 26.4 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (32): xml_etree_parse, sphinx, json, logging_format, async_tree_io, async_tree_memoization_tg, sympy_sum, coverage, genshi_xml, asyncio_websockets, sympy_integrate, richards, deepcopy, scimark_lu, 2to3, logging_simple, thrift, pylint, xml_etree_process, pprint_pformat, sqlglot_v2_normalize, genshi_text, xml_etree_generate, nbody, json_dumps, pickle_pure_python, html5lib, connected_components, shortest_path, pycparser, async_tree_io_tg, k_core

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 65.26% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x