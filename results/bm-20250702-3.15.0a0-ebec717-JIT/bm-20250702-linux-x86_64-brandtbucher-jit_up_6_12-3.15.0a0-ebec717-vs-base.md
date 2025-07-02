# Results vs. base

- fork: brandtbucher
- ref: jit_up_6_12
- machine: linux-x86_64
- commit hash: ebec717
- commit date: 2025-07-02
- overall geometric mean: 1.001x faster
- HPT reliability: 80.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                | 263 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none            | 265 ms                                                                | 257 ms: 1.03x faster                                               |
| async_tree_io              | 618 ms                                                                | 602 ms: 1.03x faster                                               |
| coroutines                 | 24.9 ms                                                               | 25.0 ms: 1.01x slower                                              |
| async_tree_none_tg         | 250 ms                                                                | 252 ms: 1.01x slower                                               |
| async_generators           | 426 ms                                                                | 431 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 486 ms                                                                | 502 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed_tg | 486 ms                                                                | 504 ms: 1.04x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                       |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 65.0 ms                                                               | 65.3 ms: 1.00x slower                                              |
| nbody          | 92.8 ms                                                               | 94.1 ms: 1.01x slower                                              |
| pidigits       | 189 ms                                                                | 201 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 23.4 ms                                                               | 22.5 ms: 1.04x faster                                              |
| regex_effbot   | 3.31 ms                                                               | 3.20 ms: 1.03x faster                                              |
| regex_dna      | 212 ms                                                                | 206 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 196 us                                                                | 190 us: 1.03x faster                                               |
| json_dumps           | 11.4 ms                                                               | 11.1 ms: 1.03x faster                                              |
| json_loads           | 28.2 us                                                               | 28.1 us: 1.00x faster                                              |
| xml_etree_parse      | 140 ms                                                                | 141 ms: 1.01x slower                                               |
| pickle_pure_python   | 320 us                                                                | 327 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_iterparse, xml_etree_process, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                              |
| python_startup_no_site | 6.94 ms                                                               | 6.96 ms: 1.00x slower                                              |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 21.9 ms                                                               | 21.2 ms: 1.03x faster                                              |
| django_template | 32.5 ms                                                               | 32.8 ms: 1.01x slower                                              |
| mako            | 10.4 ms                                                               | 10.6 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| richards_super             | 38.4 ms                                                               | 36.2 ms: 1.06x faster                                              |
| pprint_safe_repr           | 717 ms                                                                | 689 ms: 1.04x faster                                               |
| regex_v8                   | 23.4 ms                                                               | 22.5 ms: 1.04x faster                                              |
| regex_effbot               | 3.31 ms                                                               | 3.20 ms: 1.03x faster                                              |
| async_tree_none            | 265 ms                                                                | 257 ms: 1.03x faster                                               |
| unpickle_pure_python       | 196 us                                                                | 190 us: 1.03x faster                                               |
| genshi_text                | 21.9 ms                                                               | 21.2 ms: 1.03x faster                                              |
| telco                      | 165 ms                                                                | 160 ms: 1.03x faster                                               |
| json_dumps                 | 11.4 ms                                                               | 11.1 ms: 1.03x faster                                              |
| regex_dna                  | 212 ms                                                                | 206 ms: 1.03x faster                                               |
| richards                   | 32.8 ms                                                               | 32.0 ms: 1.03x faster                                              |
| async_tree_io              | 618 ms                                                                | 602 ms: 1.03x faster                                               |
| sqlglot_v2_parse           | 1.27 ms                                                               | 1.25 ms: 1.02x faster                                              |
| crypto_pyaes               | 73.8 ms                                                               | 72.4 ms: 1.02x faster                                              |
| pprint_pformat             | 1.43 sec                                                              | 1.41 sec: 1.02x faster                                             |
| nqueens                    | 84.8 ms                                                               | 83.5 ms: 1.02x faster                                              |
| deepcopy_reduce            | 2.78 us                                                               | 2.74 us: 1.01x faster                                              |
| shortest_path              | 499 ms                                                                | 492 ms: 1.01x faster                                               |
| hexiom                     | 6.19 ms                                                               | 6.13 ms: 1.01x faster                                              |
| subparsers                 | 23.9 ms                                                               | 23.7 ms: 1.01x faster                                              |
| sqlglot_v2_normalize       | 107 ms                                                                | 106 ms: 1.01x faster                                               |
| mdp                        | 1.24 sec                                                              | 1.23 sec: 1.01x faster                                             |
| logging_simple             | 5.72 us                                                               | 5.68 us: 1.01x faster                                              |
| logging_format             | 6.38 us                                                               | 6.33 us: 1.01x faster                                              |
| sqlglot_v2_transpile       | 1.58 ms                                                               | 1.57 ms: 1.01x faster                                              |
| sympy_expand               | 470 ms                                                                | 467 ms: 1.01x faster                                               |
| sqlglot_v2_optimize        | 53.0 ms                                                               | 52.8 ms: 1.01x faster                                              |
| json_loads                 | 28.2 us                                                               | 28.1 us: 1.00x faster                                              |
| comprehensions             | 16.4 us                                                               | 16.4 us: 1.00x faster                                              |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                              |
| gc_traversal               | 5.13 ms                                                               | 5.13 ms: 1.00x slower                                              |
| python_startup_no_site     | 6.94 ms                                                               | 6.96 ms: 1.00x slower                                              |
| deepcopy_memo              | 29.5 us                                                               | 29.6 us: 1.00x slower                                              |
| float                      | 65.0 ms                                                               | 65.3 ms: 1.00x slower                                              |
| coroutines                 | 24.9 ms                                                               | 25.0 ms: 1.01x slower                                              |
| create_gc_cycles           | 2.62 ms                                                               | 2.63 ms: 1.01x slower                                              |
| fannkuch                   | 400 ms                                                                | 403 ms: 1.01x slower                                               |
| bpe_tokeniser              | 4.33 sec                                                              | 4.36 sec: 1.01x slower                                             |
| deltablue                  | 3.07 ms                                                               | 3.10 ms: 1.01x slower                                              |
| meteor_contest             | 104 ms                                                                | 105 ms: 1.01x slower                                               |
| generators                 | 30.0 ms                                                               | 30.3 ms: 1.01x slower                                              |
| async_tree_none_tg         | 250 ms                                                                | 252 ms: 1.01x slower                                               |
| sympy_integrate            | 19.5 ms                                                               | 19.7 ms: 1.01x slower                                              |
| scimark_fft                | 313 ms                                                                | 316 ms: 1.01x slower                                               |
| django_template            | 32.5 ms                                                               | 32.8 ms: 1.01x slower                                              |
| xml_etree_parse            | 140 ms                                                                | 141 ms: 1.01x slower                                               |
| async_generators           | 426 ms                                                                | 431 ms: 1.01x slower                                               |
| coverage                   | 87.2 ms                                                               | 88.2 ms: 1.01x slower                                              |
| 2to3                       | 260 ms                                                                | 263 ms: 1.01x slower                                               |
| nbody                      | 92.8 ms                                                               | 94.1 ms: 1.01x slower                                              |
| logging_silent             | 101 ns                                                                | 102 ns: 1.02x slower                                               |
| sympy_sum                  | 151 ms                                                                | 154 ms: 1.02x slower                                               |
| mako                       | 10.4 ms                                                               | 10.6 ms: 1.02x slower                                              |
| pickle_pure_python         | 320 us                                                                | 327 us: 1.02x slower                                               |
| sqlite_synth               | 2.79 us                                                               | 2.86 us: 1.02x slower                                              |
| djangocms                  | 22.7 us                                                               | 23.2 us: 1.02x slower                                              |
| spectral_norm              | 90.9 ms                                                               | 93.1 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed    | 486 ms                                                                | 502 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed_tg | 486 ms                                                                | 504 ms: 1.04x slower                                               |
| scimark_sparse_mat_mult    | 4.90 ms                                                               | 5.17 ms: 1.06x slower                                              |
| pidigits                   | 189 ms                                                                | 201 ms: 1.07x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (32): pycparser, sphinx, xml_etree_generate, html5lib, go, xml_etree_iterparse, k_core, pyflate, scimark_monte_carlo, asyncio_websockets, chaos, dulwich_log, async_tree_io_tg, async_tree_memoization_tg, genshi_xml, thrift, xml_etree_process, docutils, raytrace, regex_compile, json, deepcopy, tomli_loads, scimark_sor, sympy_str, many_optionals, async_tree_memoization, pathlib, connected_components, scimark_lu, typing_runtime_protocols, pylint

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 80.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x