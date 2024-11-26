# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_8192
- machine: linux-x86_64
- commit hash: 1236a9d
- commit date: 2024-11-12
- overall geometric mean: 1.010x faster
- HPT reliability: 63.52%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 258 ms: 1.03x faster                                                |
| docutils       | 2.59 sec                                               | 2.86 sec: 1.10x slower                                              |
| html5lib       | 64.2 ms                                                | 66.6 ms: 1.04x slower                                               |
| sphinx         | 1.03 sec                                               | 1.13 sec: 1.09x slower                                              |
| Geometric mean | (ref)                                                  | 1.05x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 378 ms: 1.23x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                                |
| async_tree_none            | 351 ms                                                 | 332 ms: 1.06x faster                                                |
| async_tree_io              | 842 ms                                                 | 860 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 566 ms: 1.04x slower                                                |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 977 ms: 1.14x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (4): coroutines, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.9 ms: 1.05x faster                                               |
| float          | 79.2 ms                                                | 76.6 ms: 1.03x faster                                               |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                               |
| regex_effbot   | 3.73 ms                                                | 3.59 ms: 1.04x faster                                               |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                                |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 195 us: 1.11x faster                                                |
| xml_etree_generate   | 86.7 ms                                                | 78.9 ms: 1.10x faster                                               |
| tomli_loads          | 2.14 sec                                               | 1.96 sec: 1.09x faster                                              |
| xml_etree_process    | 60.6 ms                                                | 55.5 ms: 1.09x faster                                               |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                               |
| xml_etree_parse      | 156 ms                                                 | 158 ms: 1.01x slower                                                |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.02x slower                                                |
| pickle_pure_python   | 310 us                                                 | 318 us: 1.03x slower                                                |
| json_dumps           | 10.6 ms                                                | 11.0 ms: 1.05x slower                                               |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                               |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.09x faster                                               |
| django_template | 35.2 ms                                                | 35.6 ms: 1.01x slower                                               |
| genshi_text     | 23.5 ms                                                | 24.4 ms: 1.04x slower                                               |
| genshi_xml      | 50.9 ms                                                | 56.0 ms: 1.10x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| richards                   | 48.7 ms                                                | 36.7 ms: 1.33x faster                                               |
| deepcopy                   | 358 us                                                 | 270 us: 1.33x faster                                                |
| richards_super             | 54.9 ms                                                | 41.8 ms: 1.31x faster                                               |
| deepcopy_memo              | 39.1 us                                                | 30.0 us: 1.30x faster                                               |
| async_tree_memoization_tg  | 464 ms                                                 | 378 ms: 1.23x faster                                                |
| deepcopy_reduce            | 3.20 us                                                | 2.73 us: 1.17x faster                                               |
| scimark_fft                | 364 ms                                                 | 320 ms: 1.14x faster                                                |
| telco                      | 8.54 ms                                                | 7.57 ms: 1.13x faster                                               |
| crypto_pyaes               | 75.3 ms                                                | 68.0 ms: 1.11x faster                                               |
| unpickle_pure_python       | 216 us                                                 | 195 us: 1.11x faster                                                |
| xml_etree_generate         | 86.7 ms                                                | 78.9 ms: 1.10x faster                                               |
| go                         | 144 ms                                                 | 131 ms: 1.10x faster                                                |
| tomli_loads                | 2.14 sec                                               | 1.96 sec: 1.09x faster                                              |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.09x faster                                               |
| xml_etree_process          | 60.6 ms                                                | 55.5 ms: 1.09x faster                                               |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.09x faster                                               |
| json                       | 5.36 ms                                                | 4.97 ms: 1.08x faster                                               |
| mdp                        | 2.72 sec                                               | 2.55 sec: 1.07x faster                                              |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                                |
| logging_format             | 6.40 us                                                | 6.05 us: 1.06x faster                                               |
| async_tree_none            | 351 ms                                                 | 332 ms: 1.06x faster                                                |
| bpe_tokeniser              | 4.75 sec                                               | 4.50 sec: 1.06x faster                                              |
| scimark_monte_carlo        | 67.4 ms                                                | 64.0 ms: 1.05x faster                                               |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.80 ms: 1.05x faster                                               |
| nbody                      | 87.0 ms                                                | 82.9 ms: 1.05x faster                                               |
| thrift                     | 809 us                                                 | 776 us: 1.04x faster                                                |
| regex_effbot               | 3.73 ms                                                | 3.59 ms: 1.04x faster                                               |
| float                      | 79.2 ms                                                | 76.6 ms: 1.03x faster                                               |
| logging_simple             | 5.72 us                                                | 5.53 us: 1.03x faster                                               |
| pyflate                    | 471 ms                                                 | 455 ms: 1.03x faster                                                |
| 2to3                       | 267 ms                                                 | 258 ms: 1.03x faster                                                |
| fannkuch                   | 404 ms                                                 | 392 ms: 1.03x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                |
| scimark_sor                | 124 ms                                                 | 121 ms: 1.02x faster                                                |
| connected_components       | 444 ms                                                 | 436 ms: 1.02x faster                                                |
| logging_silent             | 102 ns                                                 | 100.0 ns: 1.02x faster                                              |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                                |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                                |
| deltablue                  | 3.23 ms                                                | 3.20 ms: 1.01x faster                                               |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                               |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x faster                                                |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| meteor_contest             | 109 ms                                                 | 109 ms: 1.00x slower                                                |
| pprint_safe_repr           | 728 ms                                                 | 734 ms: 1.01x slower                                                |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                                |
| coverage                   | 84.0 ms                                                | 84.9 ms: 1.01x slower                                               |
| django_template            | 35.2 ms                                                | 35.6 ms: 1.01x slower                                               |
| python_startup_no_site     | 6.96 ms                                                | 7.04 ms: 1.01x slower                                               |
| xml_etree_parse            | 156 ms                                                 | 158 ms: 1.01x slower                                                |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.01x slower                                                |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                               |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.02x slower                                                |
| pprint_pformat             | 1.49 sec                                               | 1.52 sec: 1.02x slower                                              |
| sqlglot_optimize           | 53.7 ms                                                | 54.8 ms: 1.02x slower                                               |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                |
| async_tree_io              | 842 ms                                                 | 860 ms: 1.02x slower                                                |
| chaos                      | 58.1 ms                                                | 59.5 ms: 1.02x slower                                               |
| pickle_pure_python         | 310 us                                                 | 318 us: 1.03x slower                                                |
| raytrace                   | 267 ms                                                 | 275 ms: 1.03x slower                                                |
| sqlglot_transpile          | 1.58 ms                                                | 1.63 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 566 ms: 1.04x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 20.7 ms: 1.04x slower                                               |
| genshi_text                | 23.5 ms                                                | 24.4 ms: 1.04x slower                                               |
| html5lib                   | 64.2 ms                                                | 66.6 ms: 1.04x slower                                               |
| dulwich_log                | 64.3 ms                                                | 67.0 ms: 1.04x slower                                               |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.04x slower                                                |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                                |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                               |
| json_dumps                 | 10.6 ms                                                | 11.0 ms: 1.05x slower                                               |
| sympy_str                  | 275 ms                                                 | 289 ms: 1.05x slower                                                |
| bench_thread_pool          | 822 us                                                 | 867 us: 1.06x slower                                                |
| comprehensions             | 16.5 us                                                | 17.5 us: 1.06x slower                                               |
| sympy_expand               | 463 ms                                                 | 500 ms: 1.08x slower                                                |
| sphinx                     | 1.03 sec                                               | 1.13 sec: 1.09x slower                                              |
| gc_traversal               | 4.37 ms                                                | 4.80 ms: 1.10x slower                                               |
| genshi_xml                 | 50.9 ms                                                | 56.0 ms: 1.10x slower                                               |
| docutils                   | 2.59 sec                                               | 2.86 sec: 1.10x slower                                              |
| create_gc_cycles           | 2.41 ms                                                | 2.69 ms: 1.12x slower                                               |
| hexiom                     | 6.16 ms                                                | 7.02 ms: 1.14x slower                                               |
| nqueens                    | 78.4 ms                                                | 89.3 ms: 1.14x slower                                               |
| async_tree_io_tg           | 857 ms                                                 | 977 ms: 1.14x slower                                                |
| generators                 | 29.0 ms                                                | 36.3 ms: 1.25x slower                                               |
| k_core                     | 2.35 sec                                               | 3.62 sec: 1.54x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 78.2 ms: 3.26x slower                                               |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (8): pycparser, coroutines, asyncio_websockets, shortest_path, async_tree_cpu_io_mixed, sqlalchemy_imperative, async_tree_none_tg, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241112-3.14.0a1+-1236a9d-JIT/bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d.json: sqlite_synth

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 63.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x