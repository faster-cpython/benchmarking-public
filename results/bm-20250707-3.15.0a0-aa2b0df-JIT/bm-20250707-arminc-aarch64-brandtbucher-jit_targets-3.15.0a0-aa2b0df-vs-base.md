# Results vs. base

- fork: brandtbucher
- ref: jit_targets
- machine: linux-aarch64
- commit hash: aa2b0df
- commit date: 2025-07-07
- overall geometric mean: 1.044x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 310 ms                                                                  | 319 ms: 1.03x slower                                                 |
| docutils       | 3.11 sec                                                                | 3.17 sec: 1.02x slower                                               |
| sphinx         | 1.15 sec                                                                | 1.18 sec: 1.02x slower                                               |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 385 ms                                                                  | 389 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg | 655 ms                                                                  | 672 ms: 1.03x slower                                                 |
| async_tree_io_tg           | 902 ms                                                                  | 926 ms: 1.03x slower                                                 |
| async_tree_io              | 905 ms                                                                  | 930 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed    | 667 ms                                                                  | 685 ms: 1.03x slower                                                 |
| async_generators           | 481 ms                                                                  | 496 ms: 1.03x slower                                                 |
| async_tree_none            | 383 ms                                                                  | 398 ms: 1.04x slower                                                 |
| async_tree_memoization     | 476 ms                                                                  | 497 ms: 1.04x slower                                                 |
| Geometric mean             | (ref)                                                                   | 1.02x slower                                                         |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_memoization_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 82.4 ms                                                                 | 89.0 ms: 1.08x slower                                                |
| nbody          | 127 ms                                                                  | 143 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                                   | 1.07x slower                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 123 ms                                                                  | 126 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                         |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process    | 77.9 ms                                                                 | 81.9 ms: 1.05x slower                                                |
| pickle_pure_python   | 400 us                                                                  | 427 us: 1.07x slower                                                 |
| tomli_loads          | 2.31 sec                                                                | 2.57 sec: 1.11x slower                                               |
| unpickle_pure_python | 250 us                                                                  | 299 us: 1.20x slower                                                 |
| Geometric mean       | (ref)                                                                   | 1.05x slower                                                         |

Benchmark hidden because not significant (5): json_dumps, xml_etree_parse, xml_etree_iterparse, json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 15.0 ms                                                                 | 15.2 ms: 1.01x slower                                                |
| python_startup_no_site | 8.60 ms                                                                 | 8.78 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                                   | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 63.2 ms                                                                 | 65.8 ms: 1.04x slower                                                |
| mako           | 13.1 ms                                                                 | 15.2 ms: 1.16x slower                                                |
| Geometric mean | (ref)                                                                   | 1.06x slower                                                         |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250707-arminc-aarch64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| logging_format             | 7.79 us                                                                 | 7.62 us: 1.02x faster                                                |
| mdp                        | 1.69 sec                                                                | 1.66 sec: 1.02x faster                                               |
| coverage                   | 101 ms                                                                  | 102 ms: 1.01x slower                                                 |
| async_tree_none_tg         | 385 ms                                                                  | 389 ms: 1.01x slower                                                 |
| python_startup             | 15.0 ms                                                                 | 15.2 ms: 1.01x slower                                                |
| logging_silent             | 128 ns                                                                  | 130 ns: 1.02x slower                                                 |
| python_startup_no_site     | 8.60 ms                                                                 | 8.78 ms: 1.02x slower                                                |
| docutils                   | 3.11 sec                                                                | 3.17 sec: 1.02x slower                                               |
| k_core                     | 2.84 sec                                                                | 2.90 sec: 1.02x slower                                               |
| sympy_sum                  | 148 ms                                                                  | 152 ms: 1.02x slower                                                 |
| sphinx                     | 1.15 sec                                                                | 1.18 sec: 1.02x slower                                               |
| shortest_path              | 597 ms                                                                  | 611 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 655 ms                                                                  | 672 ms: 1.03x slower                                                 |
| async_tree_io_tg           | 902 ms                                                                  | 926 ms: 1.03x slower                                                 |
| async_tree_io              | 905 ms                                                                  | 930 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed    | 667 ms                                                                  | 685 ms: 1.03x slower                                                 |
| 2to3                       | 310 ms                                                                  | 319 ms: 1.03x slower                                                 |
| deepcopy_memo              | 36.7 us                                                                 | 37.8 us: 1.03x slower                                                |
| regex_compile              | 123 ms                                                                  | 126 ms: 1.03x slower                                                 |
| async_generators           | 481 ms                                                                  | 496 ms: 1.03x slower                                                 |
| sqlite_synth               | 3.74 us                                                                 | 3.85 us: 1.03x slower                                                |
| raytrace                   | 331 ms                                                                  | 343 ms: 1.04x slower                                                 |
| async_tree_none            | 383 ms                                                                  | 398 ms: 1.04x slower                                                 |
| pathlib                    | 22.3 ms                                                                 | 23.2 ms: 1.04x slower                                                |
| sqlglot_v2_normalize       | 126 ms                                                                  | 131 ms: 1.04x slower                                                 |
| genshi_xml                 | 63.2 ms                                                                 | 65.8 ms: 1.04x slower                                                |
| async_tree_memoization     | 476 ms                                                                  | 497 ms: 1.04x slower                                                 |
| sympy_str                  | 275 ms                                                                  | 288 ms: 1.05x slower                                                 |
| xml_etree_process          | 77.9 ms                                                                 | 81.9 ms: 1.05x slower                                                |
| sqlglot_v2_optimize        | 62.2 ms                                                                 | 65.6 ms: 1.05x slower                                                |
| pycparser                  | 1.35 sec                                                                | 1.44 sec: 1.06x slower                                               |
| pickle_pure_python         | 400 us                                                                  | 427 us: 1.07x slower                                                 |
| float                      | 82.4 ms                                                                 | 89.0 ms: 1.08x slower                                                |
| typing_runtime_protocols   | 204 us                                                                  | 221 us: 1.09x slower                                                 |
| sqlglot_v2_transpile       | 1.84 ms                                                                 | 2.00 ms: 1.09x slower                                                |
| bpe_tokeniser              | 5.40 sec                                                                | 5.89 sec: 1.09x slower                                               |
| scimark_fft                | 409 ms                                                                  | 447 ms: 1.09x slower                                                 |
| scimark_monte_carlo        | 80.7 ms                                                                 | 88.8 ms: 1.10x slower                                                |
| tomli_loads                | 2.31 sec                                                                | 2.57 sec: 1.11x slower                                               |
| richards                   | 45.6 ms                                                                 | 51.0 ms: 1.12x slower                                                |
| nbody                      | 127 ms                                                                  | 143 ms: 1.13x slower                                                 |
| sqlglot_v2_parse           | 1.50 ms                                                                 | 1.70 ms: 1.13x slower                                                |
| pyflate                    | 525 ms                                                                  | 596 ms: 1.13x slower                                                 |
| meteor_contest             | 112 ms                                                                  | 128 ms: 1.14x slower                                                 |
| comprehensions             | 22.0 us                                                                 | 25.3 us: 1.15x slower                                                |
| richards_super             | 50.4 ms                                                                 | 58.1 ms: 1.15x slower                                                |
| crypto_pyaes               | 93.3 ms                                                                 | 108 ms: 1.16x slower                                                 |
| mako                       | 13.1 ms                                                                 | 15.2 ms: 1.16x slower                                                |
| deltablue                  | 3.86 ms                                                                 | 4.55 ms: 1.18x slower                                                |
| spectral_norm              | 120 ms                                                                  | 143 ms: 1.19x slower                                                 |
| unpickle_pure_python       | 250 us                                                                  | 299 us: 1.20x slower                                                 |
| hexiom                     | 7.70 ms                                                                 | 9.22 ms: 1.20x slower                                                |
| fannkuch                   | 473 ms                                                                  | 567 ms: 1.20x slower                                                 |
| pprint_safe_repr           | 1.15 sec                                                                | 1.39 sec: 1.21x slower                                               |
| pprint_pformat             | 2.34 sec                                                                | 2.84 sec: 1.21x slower                                               |
| go                         | 156 ms                                                                  | 198 ms: 1.27x slower                                                 |
| Geometric mean             | (ref)                                                                   | 1.05x slower                                                         |

Benchmark hidden because not significant (37): regex_v8, gc_traversal, telco, json_dumps, generators, connected_components, json, pylint, thrift, create_gc_cycles, deepcopy_reduce, html5lib, djangocms, pidigits, asyncio_websockets, xml_etree_parse, xml_etree_iterparse, regex_effbot, many_optionals, chaos, async_tree_memoization_tg, regex_dna, json_loads, coroutines, dulwich_log, subparsers, logging_simple, scimark_sor, django_template, xml_etree_generate, deepcopy, scimark_lu, sympy_expand, genshi_text, nqueens, sympy_integrate, scimark_sparse_mat_mult

- Geometric mean (including insignificant results): 1.044x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x