# Results vs. 3.13.0

- fork: methane
- ref: optimize_json_encode
- machine: linux-x86_64
- commit hash: d026be3
- commit date: 2025-04-30
- overall geometric mean: 1.051x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.06x faster                                                    |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                  |
| html5lib       | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 608 ms: 1.42x faster                                                    |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                    |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 503 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 494 ms: 1.10x faster                                                    |
| async_generators           | 433 ms                                                 | 401 ms: 1.08x faster                                                    |
| coroutines                 | 22.2 ms                                                | 25.2 ms: 1.13x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.5 ms: 1.13x faster                                                   |
| pidigits       | 186 ms                                                 | 195 ms: 1.04x slower                                                    |
| nbody          | 87.7 ms                                                | 101 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                   |
| regex_v8       | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                   |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                    |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.08x faster                                                    |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                                    |
| xml_etree_process    | 60.5 ms                                                | 60.8 ms: 1.00x slower                                                   |
| xml_etree_generate   | 86.8 ms                                                | 87.6 ms: 1.01x slower                                                   |
| json_dumps           | 10.1 ms                                                | 10.2 ms: 1.01x slower                                                   |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                    |
| pickle_pure_python   | 302 us                                                 | 311 us: 1.03x slower                                                    |
| json_loads           | 27.2 us                                                | 30.0 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.87 ms: 1.02x faster                                                   |
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                   |
| genshi_xml      | 50.5 ms                                                | 48.9 ms: 1.03x faster                                                   |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                   |
| mako            | 10.7 ms                                                | 11.7 ms: 1.10x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.08x faster                                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 608 ms: 1.42x faster                                                    |
| deepcopy                   | 354 us                                                 | 251 us: 1.41x faster                                                    |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                    |
| deepcopy_memo              | 38.4 us                                                | 28.5 us: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                    |
| go                         | 141 ms                                                 | 112 ms: 1.26x faster                                                    |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 503 ms: 1.14x faster                                                    |
| float                      | 78.7 ms                                                | 69.5 ms: 1.13x faster                                                   |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 494 ms: 1.10x faster                                                    |
| richards                   | 47.5 ms                                                | 43.2 ms: 1.10x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 59.5 ms: 1.09x faster                                                   |
| spectral_norm              | 113 ms                                                 | 105 ms: 1.08x faster                                                    |
| telco                      | 8.40 ms                                                | 7.76 ms: 1.08x faster                                                   |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                   |
| richards_super             | 53.7 ms                                                | 49.7 ms: 1.08x faster                                                   |
| async_generators           | 433 ms                                                 | 401 ms: 1.08x faster                                                    |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.08x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                  |
| pyflate                    | 470 ms                                                 | 440 ms: 1.07x faster                                                    |
| gc_traversal               | 4.90 ms                                                | 4.62 ms: 1.06x faster                                                   |
| 2to3                       | 266 ms                                                 | 252 ms: 1.06x faster                                                    |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                  |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                    |
| logging_silent             | 101 ns                                                 | 96.6 ns: 1.05x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.04x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 48.9 ms: 1.03x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 72.8 ms: 1.03x faster                                                   |
| scimark_fft                | 367 ms                                                 | 358 ms: 1.02x faster                                                    |
| chaos                      | 58.0 ms                                                | 56.6 ms: 1.02x faster                                                   |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                    |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.84 us: 1.02x faster                                                   |
| html5lib                   | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                   |
| python_startup_no_site     | 7.00 ms                                                | 6.87 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.94 ms: 1.02x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.55 us: 1.02x faster                                                   |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                                    |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                                  |
| pprint_safe_repr           | 727 ms                                                 | 721 ms: 1.01x faster                                                    |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                    |
| logging_format             | 6.23 us                                                | 6.19 us: 1.01x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 60.8 ms: 1.00x slower                                                   |
| raytrace                   | 262 ms                                                 | 263 ms: 1.01x slower                                                    |
| shortest_path              | 487 ms                                                 | 490 ms: 1.01x slower                                                    |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                                   |
| xml_etree_generate         | 86.8 ms                                                | 87.6 ms: 1.01x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 10.2 ms: 1.01x slower                                                   |
| connected_components       | 447 ms                                                 | 452 ms: 1.01x slower                                                    |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 67.7 ms: 1.01x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                    |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                    |
| hexiom                     | 6.08 ms                                                | 6.18 ms: 1.02x slower                                                   |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                   |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.03x slower                                                   |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 311 us: 1.03x slower                                                    |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                   |
| pidigits                   | 186 ms                                                 | 195 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                    |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                                    |
| deltablue                  | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                   |
| json                       | 5.32 ms                                                | 5.62 ms: 1.06x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 887 us: 1.08x slower                                                    |
| many_optionals             | 857 us                                                 | 933 us: 1.09x slower                                                    |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.10x slower                                                   |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.10x slower                                                   |
| coverage                   | 82.8 ms                                                | 92.5 ms: 1.12x slower                                                   |
| coroutines                 | 22.2 ms                                                | 25.2 ms: 1.13x slower                                                   |
| nbody                      | 87.7 ms                                                | 101 ms: 1.15x slower                                                    |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.36x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 82.0 ms: 3.42x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (4): sphinx, nqueens, sympy_expand, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250430-3.14.0a7+-d026be3/bm-20250430-linux-x86_64-methane-optimize_json_encode-3.14.0a7+-d026be3.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x