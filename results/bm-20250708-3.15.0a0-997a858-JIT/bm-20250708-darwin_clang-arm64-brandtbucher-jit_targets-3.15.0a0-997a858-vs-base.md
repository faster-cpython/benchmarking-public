# Results vs. base

- fork: brandtbucher
- ref: jit_targets
- machine: darwin-arm64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.017x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250707-darwin_clang-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 162 ms                                                                      | 160 ms: 1.01x faster                                                     |
| docutils       | 1.40 sec                                                                    | 1.39 sec: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                             |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250707-darwin_clang-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_eager           | 59.3 ms                                                                     | 57.0 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 408 ms                                                                      | 403 ms: 1.01x faster                                                     |
| async_tree_io              | 344 ms                                                                      | 340 ms: 1.01x faster                                                     |
| async_tree_memoization     | 180 ms                                                                      | 179 ms: 1.01x faster                                                     |
| async_generators           | 271 ms                                                                      | 269 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed    | 407 ms                                                                      | 405 ms: 1.00x faster                                                     |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (13): async_tree_none, async_tree_eager_memoization, async_tree_none_tg, async_tree_eager_tg, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, asyncio_websockets, async_tree_eager_io, async_tree_eager_cpu_io_mixed_tg, async_tree_io_tg, async_tree_eager_memoization_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250707-darwin_clang-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 76.1 ms                                                                     | 73.2 ms: 1.04x faster                                                    |
| float          | 44.5 ms                                                                     | 44.7 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250707-darwin_clang-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 62.9 ms                                                                     | 62.4 ms: 1.01x faster                                                    |
| regex_effbot   | 2.47 ms                                                                     | 2.48 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250707-darwin_clang-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 131 us                                                                      | 124 us: 1.06x faster                                                     |
| tomli_loads          | 1.18 sec                                                                    | 1.13 sec: 1.05x faster                                                   |
| pickle_pure_python   | 191 us                                                                      | 185 us: 1.03x faster                                                     |
| xml_etree_process    | 34.2 ms                                                                     | 33.3 ms: 1.03x faster                                                    |
| xml_etree_generate   | 49.5 ms                                                                     | 48.9 ms: 1.01x faster                                                    |
| json_loads           | 16.7 us                                                                     | 16.8 us: 1.00x slower                                                    |
| xml_etree_iterparse  | 70.3 ms                                                                     | 70.7 ms: 1.00x slower                                                    |
| xml_etree_parse      | 103 ms                                                                      | 103 ms: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                                       | 1.02x faster                                                             |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250707-darwin_clang-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 14.4 ms                                                                     | 14.4 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250707-darwin_clang-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 6.90 ms                                                                     | 6.64 ms: 1.04x faster                                                    |
| django_template | 19.9 ms                                                                     | 19.7 ms: 1.01x faster                                                    |
| genshi_text     | 12.6 ms                                                                     | 12.7 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250707-darwin_clang-arm64-python-0240ef4705d835e27beb-3.15.0a0-0240ef4 | bm-20250708-darwin_clang-arm64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pprint_pformat             | 1.02 sec                                                                    | 832 ms: 1.22x faster                                                     |
| pprint_safe_repr           | 504 ms                                                                      | 414 ms: 1.22x faster                                                     |
| fannkuch                   | 304 ms                                                                      | 259 ms: 1.18x faster                                                     |
| scimark_sparse_mat_mult    | 3.62 ms                                                                     | 3.33 ms: 1.09x faster                                                    |
| comprehensions             | 11.4 us                                                                     | 10.6 us: 1.08x faster                                                    |
| hexiom                     | 4.47 ms                                                                     | 4.17 ms: 1.07x faster                                                    |
| unpickle_pure_python       | 131 us                                                                      | 124 us: 1.06x faster                                                     |
| scimark_fft                | 201 ms                                                                      | 190 ms: 1.06x faster                                                     |
| typing_runtime_protocols   | 92.8 us                                                                     | 88.3 us: 1.05x faster                                                    |
| tomli_loads                | 1.18 sec                                                                    | 1.13 sec: 1.05x faster                                                   |
| sqlglot_v2_parse           | 752 us                                                                      | 719 us: 1.05x faster                                                     |
| bpe_tokeniser              | 3.07 sec                                                                    | 2.94 sec: 1.04x faster                                                   |
| spectral_norm              | 66.7 ms                                                                     | 64.0 ms: 1.04x faster                                                    |
| telco                      | 4.61 ms                                                                     | 4.42 ms: 1.04x faster                                                    |
| async_tree_eager           | 59.3 ms                                                                     | 57.0 ms: 1.04x faster                                                    |
| nbody                      | 76.1 ms                                                                     | 73.2 ms: 1.04x faster                                                    |
| mako                       | 6.90 ms                                                                     | 6.64 ms: 1.04x faster                                                    |
| meteor_contest             | 76.0 ms                                                                     | 73.2 ms: 1.04x faster                                                    |
| crypto_pyaes               | 51.8 ms                                                                     | 50.0 ms: 1.04x faster                                                    |
| sqlglot_v2_transpile       | 905 us                                                                      | 874 us: 1.04x faster                                                     |
| pickle_pure_python         | 191 us                                                                      | 185 us: 1.03x faster                                                     |
| xml_etree_process          | 34.2 ms                                                                     | 33.3 ms: 1.03x faster                                                    |
| pycparser                  | 673 ms                                                                      | 656 ms: 1.03x faster                                                     |
| sqlglot_v2_normalize       | 63.6 ms                                                                     | 62.1 ms: 1.02x faster                                                    |
| sqlglot_v2_optimize        | 31.5 ms                                                                     | 30.9 ms: 1.02x faster                                                    |
| thrift                     | 420 us                                                                      | 413 us: 1.02x faster                                                     |
| 2to3                       | 162 ms                                                                      | 160 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed_tg | 408 ms                                                                      | 403 ms: 1.01x faster                                                     |
| go                         | 73.6 ms                                                                     | 72.7 ms: 1.01x faster                                                    |
| xml_etree_generate         | 49.5 ms                                                                     | 48.9 ms: 1.01x faster                                                    |
| sympy_integrate            | 10.3 ms                                                                     | 10.2 ms: 1.01x faster                                                    |
| async_tree_io              | 344 ms                                                                      | 340 ms: 1.01x faster                                                     |
| deltablue                  | 2.21 ms                                                                     | 2.19 ms: 1.01x faster                                                    |
| sympy_expand               | 225 ms                                                                      | 222 ms: 1.01x faster                                                     |
| sympy_sum                  | 70.7 ms                                                                     | 70.1 ms: 1.01x faster                                                    |
| regex_compile              | 62.9 ms                                                                     | 62.4 ms: 1.01x faster                                                    |
| sympy_str                  | 132 ms                                                                      | 131 ms: 1.01x faster                                                     |
| django_template            | 19.9 ms                                                                     | 19.7 ms: 1.01x faster                                                    |
| docutils                   | 1.40 sec                                                                    | 1.39 sec: 1.01x faster                                                   |
| logging_simple             | 3.00 us                                                                     | 2.98 us: 1.01x faster                                                    |
| sqlite_synth               | 1.58 us                                                                     | 1.56 us: 1.01x faster                                                    |
| async_tree_memoization     | 180 ms                                                                      | 179 ms: 1.01x faster                                                     |
| deepcopy_reduce            | 1.57 us                                                                     | 1.56 us: 1.01x faster                                                    |
| async_generators           | 271 ms                                                                      | 269 ms: 1.01x faster                                                     |
| shortest_path              | 336 ms                                                                      | 334 ms: 1.01x faster                                                     |
| logging_format             | 3.26 us                                                                     | 3.24 us: 1.01x faster                                                    |
| many_optionals             | 446 us                                                                      | 444 us: 1.00x faster                                                     |
| connected_components       | 310 ms                                                                      | 309 ms: 1.00x faster                                                     |
| scimark_sor                | 74.9 ms                                                                     | 74.6 ms: 1.00x faster                                                    |
| raytrace                   | 159 ms                                                                      | 158 ms: 1.00x faster                                                     |
| async_tree_cpu_io_mixed    | 407 ms                                                                      | 405 ms: 1.00x faster                                                     |
| python_startup_no_site     | 14.4 ms                                                                     | 14.4 ms: 1.00x faster                                                    |
| chaos                      | 35.0 ms                                                                     | 34.9 ms: 1.00x faster                                                    |
| richards                   | 29.1 ms                                                                     | 29.0 ms: 1.00x faster                                                    |
| nqueens                    | 56.7 ms                                                                     | 56.7 ms: 1.00x slower                                                    |
| json_loads                 | 16.7 us                                                                     | 16.8 us: 1.00x slower                                                    |
| create_gc_cycles           | 1.34 ms                                                                     | 1.35 ms: 1.00x slower                                                    |
| regex_effbot               | 2.47 ms                                                                     | 2.48 ms: 1.00x slower                                                    |
| xml_etree_iterparse        | 70.3 ms                                                                     | 70.7 ms: 1.00x slower                                                    |
| float                      | 44.5 ms                                                                     | 44.7 ms: 1.01x slower                                                    |
| coverage                   | 46.3 ms                                                                     | 46.6 ms: 1.01x slower                                                    |
| logging_silent             | 59.7 ns                                                                     | 60.0 ns: 1.01x slower                                                    |
| xml_etree_parse            | 103 ms                                                                      | 103 ms: 1.01x slower                                                     |
| genshi_text                | 12.6 ms                                                                     | 12.7 ms: 1.01x slower                                                    |
| Geometric mean             | (ref)                                                                       | 1.02x faster                                                             |

Benchmark hidden because not significant (37): python_startup, async_tree_none, async_tree_eager_memoization, async_tree_none_tg, k_core, async_tree_eager_tg, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, pylint, subparsers, json_dumps, deepcopy_memo, asyncio_websockets, generators, async_tree_eager_io, deepcopy, async_tree_eager_cpu_io_mixed_tg, scimark_lu, gc_traversal, pyflate, regex_dna, dask, regex_v8, async_tree_io_tg, async_tree_eager_memoization_tg, coroutines, sphinx, scimark_monte_carlo, pidigits, mdp, richards_super, json, dulwich_log, html5lib, genshi_xml, pathlib

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x