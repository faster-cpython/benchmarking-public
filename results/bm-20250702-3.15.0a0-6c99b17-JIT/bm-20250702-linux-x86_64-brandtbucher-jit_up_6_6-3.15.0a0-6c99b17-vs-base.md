# Results vs. base

- fork: brandtbucher
- ref: jit_up_6_6
- machine: linux-x86_64
- commit hash: 6c99b17
- commit date: 2025-07-02
- overall geometric mean: 1.000x slower
- HPT reliability: 61.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 260 ms                                                                | 267 ms: 1.03x slower                                              |
| docutils       | 2.66 sec                                                              | 2.69 sec: 1.01x slower                                            |
| html5lib       | 62.2 ms                                                               | 61.7 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none            | 265 ms                                                                | 255 ms: 1.04x faster                                              |
| async_tree_io              | 618 ms                                                                | 602 ms: 1.03x faster                                              |
| coroutines                 | 24.9 ms                                                               | 25.4 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed_tg | 486 ms                                                                | 500 ms: 1.03x slower                                              |
| async_tree_cpu_io_mixed    | 486 ms                                                                | 502 ms: 1.03x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io_tg, asyncio_websockets, async_tree_none_tg, async_tree_memoization, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 65.0 ms                                                               | 65.7 ms: 1.01x slower                                             |
| pidigits       | 189 ms                                                                | 193 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 23.4 ms                                                               | 23.1 ms: 1.01x faster                                             |
| regex_compile  | 128 ms                                                                | 130 ms: 1.01x slower                                              |
| regex_dna      | 212 ms                                                                | 216 ms: 1.02x slower                                              |
| regex_effbot   | 3.31 ms                                                               | 3.39 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 11.4 ms                                                               | 11.1 ms: 1.03x faster                                             |
| unpickle_pure_python | 196 us                                                                | 192 us: 1.02x faster                                              |
| xml_etree_generate   | 80.2 ms                                                               | 78.8 ms: 1.02x faster                                             |
| xml_etree_iterparse  | 99.4 ms                                                               | 98.2 ms: 1.01x faster                                             |
| tomli_loads          | 1.84 sec                                                              | 1.85 sec: 1.01x slower                                            |
| json_loads           | 28.2 us                                                               | 28.9 us: 1.03x slower                                             |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                               | 6.95 ms: 1.00x slower                                             |
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                             |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 21.9 ms                                                               | 21.5 ms: 1.02x faster                                             |
| django_template | 32.5 ms                                                               | 32.6 ms: 1.01x slower                                             |
| mako            | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                             |
| genshi_xml      | 50.5 ms                                                               | 50.9 ms: 1.01x slower                                             |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20250702-linux-x86_64-python-fa43a1e0f8caf00a1589-3.15.0a0-fa43a1e | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none            | 265 ms                                                                | 255 ms: 1.04x faster                                              |
| pyflate                    | 422 ms                                                                | 406 ms: 1.04x faster                                              |
| json_dumps                 | 11.4 ms                                                               | 11.1 ms: 1.03x faster                                             |
| pprint_pformat             | 1.43 sec                                                              | 1.39 sec: 1.03x faster                                            |
| pprint_safe_repr           | 717 ms                                                                | 698 ms: 1.03x faster                                              |
| async_tree_io              | 618 ms                                                                | 602 ms: 1.03x faster                                              |
| telco                      | 165 ms                                                                | 161 ms: 1.03x faster                                              |
| crypto_pyaes               | 73.8 ms                                                               | 72.2 ms: 1.02x faster                                             |
| raytrace                   | 276 ms                                                                | 270 ms: 1.02x faster                                              |
| genshi_text                | 21.9 ms                                                               | 21.5 ms: 1.02x faster                                             |
| gc_traversal               | 5.13 ms                                                               | 5.03 ms: 1.02x faster                                             |
| deepcopy_reduce            | 2.78 us                                                               | 2.72 us: 1.02x faster                                             |
| unpickle_pure_python       | 196 us                                                                | 192 us: 1.02x faster                                              |
| xml_etree_generate         | 80.2 ms                                                               | 78.8 ms: 1.02x faster                                             |
| hexiom                     | 6.19 ms                                                               | 6.08 ms: 1.02x faster                                             |
| shortest_path              | 499 ms                                                                | 492 ms: 1.01x faster                                              |
| comprehensions             | 16.4 us                                                               | 16.2 us: 1.01x faster                                             |
| xml_etree_iterparse        | 99.4 ms                                                               | 98.2 ms: 1.01x faster                                             |
| regex_v8                   | 23.4 ms                                                               | 23.1 ms: 1.01x faster                                             |
| sqlglot_v2_parse           | 1.27 ms                                                               | 1.26 ms: 1.01x faster                                             |
| fannkuch                   | 400 ms                                                                | 396 ms: 1.01x faster                                              |
| go                         | 116 ms                                                                | 115 ms: 1.01x faster                                              |
| chaos                      | 61.1 ms                                                               | 60.5 ms: 1.01x faster                                             |
| html5lib                   | 62.2 ms                                                               | 61.7 ms: 1.01x faster                                             |
| nqueens                    | 84.8 ms                                                               | 84.1 ms: 1.01x faster                                             |
| spectral_norm              | 90.9 ms                                                               | 90.1 ms: 1.01x faster                                             |
| meteor_contest             | 104 ms                                                                | 103 ms: 1.01x faster                                              |
| logging_simple             | 5.72 us                                                               | 5.68 us: 1.01x faster                                             |
| connected_components       | 462 ms                                                                | 459 ms: 1.01x faster                                              |
| scimark_fft                | 313 ms                                                                | 312 ms: 1.00x faster                                              |
| deltablue                  | 3.07 ms                                                               | 3.06 ms: 1.00x faster                                             |
| sqlglot_v2_normalize       | 107 ms                                                                | 106 ms: 1.00x faster                                              |
| python_startup_no_site     | 6.94 ms                                                               | 6.95 ms: 1.00x slower                                             |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                             |
| sqlglot_v2_optimize        | 53.0 ms                                                               | 53.2 ms: 1.00x slower                                             |
| sympy_str                  | 274 ms                                                                | 275 ms: 1.00x slower                                              |
| dulwich_log                | 59.5 ms                                                               | 59.8 ms: 1.00x slower                                             |
| sqlglot_v2_transpile       | 1.58 ms                                                               | 1.59 ms: 1.01x slower                                             |
| django_template            | 32.5 ms                                                               | 32.6 ms: 1.01x slower                                             |
| tomli_loads                | 1.84 sec                                                              | 1.85 sec: 1.01x slower                                            |
| mako                       | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                             |
| typing_runtime_protocols   | 169 us                                                                | 170 us: 1.01x slower                                              |
| bpe_tokeniser              | 4.33 sec                                                              | 4.37 sec: 1.01x slower                                            |
| pathlib                    | 17.0 ms                                                               | 17.2 ms: 1.01x slower                                             |
| docutils                   | 2.66 sec                                                              | 2.69 sec: 1.01x slower                                            |
| deepcopy_memo              | 29.5 us                                                               | 29.8 us: 1.01x slower                                             |
| genshi_xml                 | 50.5 ms                                                               | 50.9 ms: 1.01x slower                                             |
| float                      | 65.0 ms                                                               | 65.7 ms: 1.01x slower                                             |
| create_gc_cycles           | 2.62 ms                                                               | 2.64 ms: 1.01x slower                                             |
| many_optionals             | 989 us                                                                | 999 us: 1.01x slower                                              |
| regex_compile              | 128 ms                                                                | 130 ms: 1.01x slower                                              |
| generators                 | 30.0 ms                                                               | 30.4 ms: 1.01x slower                                             |
| json                       | 5.26 ms                                                               | 5.33 ms: 1.01x slower                                             |
| sympy_sum                  | 151 ms                                                                | 153 ms: 1.01x slower                                              |
| logging_silent             | 101 ns                                                                | 102 ns: 1.02x slower                                              |
| scimark_monte_carlo        | 66.0 ms                                                               | 67.1 ms: 1.02x slower                                             |
| sympy_integrate            | 19.5 ms                                                               | 19.8 ms: 1.02x slower                                             |
| regex_dna                  | 212 ms                                                                | 216 ms: 1.02x slower                                              |
| pidigits                   | 189 ms                                                                | 193 ms: 1.02x slower                                              |
| coroutines                 | 24.9 ms                                                               | 25.4 ms: 1.02x slower                                             |
| regex_effbot               | 3.31 ms                                                               | 3.39 ms: 1.02x slower                                             |
| richards_super             | 38.4 ms                                                               | 39.3 ms: 1.02x slower                                             |
| scimark_sor                | 117 ms                                                                | 120 ms: 1.02x slower                                              |
| scimark_sparse_mat_mult    | 4.90 ms                                                               | 5.02 ms: 1.02x slower                                             |
| json_loads                 | 28.2 us                                                               | 28.9 us: 1.03x slower                                             |
| 2to3                       | 260 ms                                                                | 267 ms: 1.03x slower                                              |
| async_tree_cpu_io_mixed_tg | 486 ms                                                                | 500 ms: 1.03x slower                                              |
| pycparser                  | 1.12 sec                                                              | 1.15 sec: 1.03x slower                                            |
| async_tree_cpu_io_mixed    | 486 ms                                                                | 502 ms: 1.03x slower                                              |
| richards                   | 32.8 ms                                                               | 34.7 ms: 1.06x slower                                             |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (23): async_tree_memoization_tg, async_tree_io_tg, sphinx, xml_etree_process, logging_format, k_core, asyncio_websockets, deepcopy, async_tree_none_tg, async_tree_memoization, subparsers, mdp, xml_etree_parse, thrift, nbody, sympy_expand, pickle_pure_python, scimark_lu, coverage, async_generators, sqlite_synth, djangocms, pylint

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 61.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x