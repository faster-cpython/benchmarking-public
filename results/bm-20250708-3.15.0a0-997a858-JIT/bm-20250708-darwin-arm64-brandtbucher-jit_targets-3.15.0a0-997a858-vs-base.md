# Results vs. base

- fork: brandtbucher
- ref: jit_targets
- machine: darwin-arm64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.016x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 172 ms                                                                | 169 ms: 1.02x faster                                               |
| docutils       | 1.45 sec                                                              | 1.44 sec: 1.01x faster                                             |
| html5lib       | 31.7 ms                                                               | 32.5 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager              | 64.1 ms                                                               | 62.9 ms: 1.02x faster                                              |
| async_tree_io                 | 375 ms                                                                | 370 ms: 1.02x faster                                               |
| async_tree_none               | 163 ms                                                                | 161 ms: 1.01x faster                                               |
| async_tree_memoization        | 194 ms                                                                | 192 ms: 1.01x faster                                               |
| async_tree_none_tg            | 156 ms                                                                | 155 ms: 1.01x faster                                               |
| async_tree_eager_cpu_io_mixed | 358 ms                                                                | 357 ms: 1.00x faster                                               |
| async_generators              | 280 ms                                                                | 280 ms: 1.00x faster                                               |
| async_tree_cpu_io_mixed       | 416 ms                                                                | 415 ms: 1.00x faster                                               |
| Geometric mean                | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (11): async_tree_io_tg, async_tree_eager_memoization, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_tg, async_tree_memoization_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 76.5 ms                                                               | 72.0 ms: 1.06x faster                                              |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                       |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 71.3 ms                                                               | 70.6 ms: 1.01x faster                                              |
| regex_dna      | 143 ms                                                                | 144 ms: 1.01x slower                                               |
| regex_effbot   | 2.34 ms                                                               | 2.35 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 134 us                                                                | 129 us: 1.04x faster                                               |
| tomli_loads          | 1.24 sec                                                              | 1.19 sec: 1.04x faster                                             |
| xml_etree_process    | 35.7 ms                                                               | 34.8 ms: 1.03x faster                                              |
| pickle_pure_python   | 210 us                                                                | 205 us: 1.03x faster                                               |
| xml_etree_generate   | 50.7 ms                                                               | 49.6 ms: 1.02x faster                                              |
| json_loads           | 16.4 us                                                               | 16.5 us: 1.01x slower                                              |
| json_dumps           | 6.57 ms                                                               | 6.65 ms: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.02x faster                                                       |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 19.1 ms                                                               | 20.5 ms: 1.07x slower                                              |
| python_startup_no_site | 14.5 ms                                                               | 15.9 ms: 1.10x slower                                              |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 6.93 ms                                                               | 6.64 ms: 1.04x faster                                              |
| django_template | 21.8 ms                                                               | 21.7 ms: 1.00x faster                                              |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                     | bm-20250707-darwin-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| fannkuch                      | 308 ms                                                                | 257 ms: 1.20x faster                                               |
| pprint_pformat                | 1.06 sec                                                              | 901 ms: 1.18x faster                                               |
| pprint_safe_repr              | 525 ms                                                                | 446 ms: 1.18x faster                                               |
| meteor_contest                | 77.6 ms                                                               | 71.6 ms: 1.08x faster                                              |
| comprehensions                | 12.1 us                                                               | 11.3 us: 1.07x faster                                              |
| hexiom                        | 4.77 ms                                                               | 4.47 ms: 1.07x faster                                              |
| nbody                         | 76.5 ms                                                               | 72.0 ms: 1.06x faster                                              |
| scimark_sparse_mat_mult       | 3.53 ms                                                               | 3.35 ms: 1.05x faster                                              |
| bpe_tokeniser                 | 3.08 sec                                                              | 2.94 sec: 1.05x faster                                             |
| telco                         | 4.62 ms                                                               | 4.41 ms: 1.05x faster                                              |
| scimark_fft                   | 199 ms                                                                | 190 ms: 1.05x faster                                               |
| typing_runtime_protocols      | 98.0 us                                                               | 93.8 us: 1.04x faster                                              |
| nqueens                       | 64.4 ms                                                               | 61.7 ms: 1.04x faster                                              |
| unpickle_pure_python          | 134 us                                                                | 129 us: 1.04x faster                                               |
| mako                          | 6.93 ms                                                               | 6.64 ms: 1.04x faster                                              |
| spectral_norm                 | 66.7 ms                                                               | 64.1 ms: 1.04x faster                                              |
| tomli_loads                   | 1.24 sec                                                              | 1.19 sec: 1.04x faster                                             |
| sqlglot_v2_transpile          | 982 us                                                                | 946 us: 1.04x faster                                               |
| pycparser                     | 705 ms                                                                | 679 ms: 1.04x faster                                               |
| crypto_pyaes                  | 55.9 ms                                                               | 53.9 ms: 1.04x faster                                              |
| shortest_path                 | 349 ms                                                                | 337 ms: 1.04x faster                                               |
| sqlglot_v2_parse              | 803 us                                                                | 777 us: 1.03x faster                                               |
| sqlite_synth                  | 1.61 us                                                               | 1.56 us: 1.03x faster                                              |
| xml_etree_process             | 35.7 ms                                                               | 34.8 ms: 1.03x faster                                              |
| pickle_pure_python            | 210 us                                                                | 205 us: 1.03x faster                                               |
| sqlglot_v2_optimize           | 33.8 ms                                                               | 33.0 ms: 1.02x faster                                              |
| xml_etree_generate            | 50.7 ms                                                               | 49.6 ms: 1.02x faster                                              |
| pyflate                       | 288 ms                                                                | 283 ms: 1.02x faster                                               |
| connected_components          | 314 ms                                                                | 308 ms: 1.02x faster                                               |
| async_tree_eager              | 64.1 ms                                                               | 62.9 ms: 1.02x faster                                              |
| 2to3                          | 172 ms                                                                | 169 ms: 1.02x faster                                               |
| sqlglot_v2_normalize          | 68.4 ms                                                               | 67.4 ms: 1.02x faster                                              |
| async_tree_io                 | 375 ms                                                                | 370 ms: 1.02x faster                                               |
| async_tree_none               | 163 ms                                                                | 161 ms: 1.01x faster                                               |
| sympy_integrate               | 11.1 ms                                                               | 11.0 ms: 1.01x faster                                              |
| sympy_sum                     | 75.7 ms                                                               | 74.8 ms: 1.01x faster                                              |
| async_tree_memoization        | 194 ms                                                                | 192 ms: 1.01x faster                                               |
| many_optionals                | 475 us                                                                | 470 us: 1.01x faster                                               |
| regex_compile                 | 71.3 ms                                                               | 70.6 ms: 1.01x faster                                              |
| thrift                        | 445 us                                                                | 440 us: 1.01x faster                                               |
| go                            | 86.8 ms                                                               | 86.1 ms: 1.01x faster                                              |
| docutils                      | 1.45 sec                                                              | 1.44 sec: 1.01x faster                                             |
| mdp                           | 761 ms                                                                | 754 ms: 1.01x faster                                               |
| subparsers                    | 13.8 ms                                                               | 13.7 ms: 1.01x faster                                              |
| async_tree_none_tg            | 156 ms                                                                | 155 ms: 1.01x faster                                               |
| chaos                         | 39.4 ms                                                               | 39.1 ms: 1.01x faster                                              |
| sympy_expand                  | 244 ms                                                                | 242 ms: 1.01x faster                                               |
| sympy_str                     | 144 ms                                                                | 143 ms: 1.01x faster                                               |
| deepcopy                      | 157 us                                                                | 156 us: 1.01x faster                                               |
| deepcopy_reduce               | 1.68 us                                                               | 1.67 us: 1.00x faster                                              |
| django_template               | 21.8 ms                                                               | 21.7 ms: 1.00x faster                                              |
| async_tree_eager_cpu_io_mixed | 358 ms                                                                | 357 ms: 1.00x faster                                               |
| raytrace                      | 179 ms                                                                | 178 ms: 1.00x faster                                               |
| async_generators              | 280 ms                                                                | 280 ms: 1.00x faster                                               |
| scimark_monte_carlo           | 46.0 ms                                                               | 45.9 ms: 1.00x faster                                              |
| async_tree_cpu_io_mixed       | 416 ms                                                                | 415 ms: 1.00x faster                                               |
| scimark_lu                    | 81.9 ms                                                               | 82.1 ms: 1.00x slower                                              |
| richards_super                | 39.2 ms                                                               | 39.3 ms: 1.00x slower                                              |
| dulwich_log                   | 25.1 ms                                                               | 25.1 ms: 1.00x slower                                              |
| regex_dna                     | 143 ms                                                                | 144 ms: 1.01x slower                                               |
| regex_effbot                  | 2.34 ms                                                               | 2.35 ms: 1.01x slower                                              |
| json_loads                    | 16.4 us                                                               | 16.5 us: 1.01x slower                                              |
| scimark_sor                   | 88.4 ms                                                               | 89.2 ms: 1.01x slower                                              |
| json_dumps                    | 6.57 ms                                                               | 6.65 ms: 1.01x slower                                              |
| html5lib                      | 31.7 ms                                                               | 32.5 ms: 1.02x slower                                              |
| python_startup                | 19.1 ms                                                               | 20.5 ms: 1.07x slower                                              |
| python_startup_no_site        | 14.5 ms                                                               | 15.9 ms: 1.10x slower                                              |
| Geometric mean                | (ref)                                                                 | 1.02x faster                                                       |

Benchmark hidden because not significant (34): async_tree_io_tg, k_core, async_tree_eager_memoization, async_tree_eager_io, async_tree_eager_io_tg, pylint, async_tree_eager_tg, async_tree_memoization_tg, xml_etree_iterparse, async_tree_eager_memoization_tg, sphinx, async_tree_cpu_io_mixed_tg, xml_etree_parse, pidigits, deepcopy_memo, gc_traversal, genshi_xml, async_tree_eager_cpu_io_mixed_tg, regex_v8, generators, dask, richards, asyncio_websockets, float, logging_simple, logging_silent, genshi_text, logging_format, coroutines, create_gc_cycles, coverage, deltablue, json, pathlib

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x