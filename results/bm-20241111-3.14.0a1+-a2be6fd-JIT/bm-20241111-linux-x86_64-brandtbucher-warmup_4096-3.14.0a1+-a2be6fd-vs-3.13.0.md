# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_4096
- machine: linux-x86_64
- commit hash: a2be6fd
- commit date: 2024-11-11
- overall geometric mean: 1.008x faster
- HPT reliability: 51.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 262 ms: 1.02x faster                                                |
| docutils       | 2.59 sec                                               | 2.89 sec: 1.11x slower                                              |
| html5lib       | 64.2 ms                                                | 66.7 ms: 1.04x slower                                               |
| sphinx         | 1.03 sec                                               | 1.14 sec: 1.10x slower                                              |
| Geometric mean | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 375 ms: 1.24x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                |
| async_tree_none            | 351 ms                                                 | 329 ms: 1.06x faster                                                |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 567 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 551 ms: 1.01x slower                                                |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                               |
| async_tree_io              | 842 ms                                                 | 860 ms: 1.02x slower                                                |
| async_generators           | 436 ms                                                 | 456 ms: 1.05x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 980 ms: 1.14x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 83.4 ms: 1.04x faster                                               |
| float          | 79.2 ms                                                | 76.3 ms: 1.04x faster                                               |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.6 ms: 1.06x faster                                               |
| regex_dna      | 218 ms                                                 | 211 ms: 1.04x faster                                                |
| regex_effbot   | 3.73 ms                                                | 3.62 ms: 1.03x faster                                               |
| regex_compile  | 132 ms                                                 | 134 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 193 us: 1.12x faster                                                |
| tomli_loads          | 2.14 sec                                               | 1.95 sec: 1.10x faster                                              |
| xml_etree_process    | 60.6 ms                                                | 56.9 ms: 1.07x faster                                               |
| xml_etree_generate   | 86.7 ms                                                | 81.7 ms: 1.06x faster                                               |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                               |
| json_dumps           | 10.6 ms                                                | 10.9 ms: 1.03x slower                                               |
| pickle_pure_python   | 310 us                                                 | 323 us: 1.04x slower                                                |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                               |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.3 ms: 1.07x faster                                               |
| django_template | 35.2 ms                                                | 36.2 ms: 1.03x slower                                               |
| genshi_text     | 23.5 ms                                                | 24.8 ms: 1.05x slower                                               |
| genshi_xml      | 50.9 ms                                                | 58.4 ms: 1.15x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 268 us: 1.34x faster                                                |
| deepcopy_memo              | 39.1 us                                                | 29.5 us: 1.32x faster                                               |
| richards                   | 48.7 ms                                                | 37.3 ms: 1.30x faster                                               |
| richards_super             | 54.9 ms                                                | 42.2 ms: 1.30x faster                                               |
| async_tree_memoization_tg  | 464 ms                                                 | 375 ms: 1.24x faster                                                |
| deepcopy_reduce            | 3.20 us                                                | 2.73 us: 1.17x faster                                               |
| scimark_fft                | 364 ms                                                 | 320 ms: 1.14x faster                                                |
| unpickle_pure_python       | 216 us                                                 | 193 us: 1.12x faster                                                |
| telco                      | 8.54 ms                                                | 7.68 ms: 1.11x faster                                               |
| crypto_pyaes               | 75.3 ms                                                | 68.3 ms: 1.10x faster                                               |
| tomli_loads                | 2.14 sec                                               | 1.95 sec: 1.10x faster                                              |
| json                       | 5.36 ms                                                | 4.90 ms: 1.09x faster                                               |
| go                         | 144 ms                                                 | 133 ms: 1.08x faster                                                |
| mako                       | 11.1 ms                                                | 10.3 ms: 1.07x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                |
| xml_etree_process          | 60.6 ms                                                | 56.9 ms: 1.07x faster                                               |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.73 ms: 1.07x faster                                               |
| async_tree_none            | 351 ms                                                 | 329 ms: 1.06x faster                                                |
| regex_v8                   | 26.2 ms                                                | 24.6 ms: 1.06x faster                                               |
| xml_etree_generate         | 86.7 ms                                                | 81.7 ms: 1.06x faster                                               |
| bpe_tokeniser              | 4.75 sec                                               | 4.48 sec: 1.06x faster                                              |
| fannkuch                   | 404 ms                                                 | 383 ms: 1.06x faster                                                |
| pathlib                    | 17.5 ms                                                | 16.6 ms: 1.05x faster                                               |
| scimark_monte_carlo        | 67.4 ms                                                | 64.4 ms: 1.05x faster                                               |
| pyflate                    | 471 ms                                                 | 451 ms: 1.04x faster                                                |
| nbody                      | 87.0 ms                                                | 83.4 ms: 1.04x faster                                               |
| logging_format             | 6.40 us                                                | 6.16 us: 1.04x faster                                               |
| float                      | 79.2 ms                                                | 76.3 ms: 1.04x faster                                               |
| thrift                     | 809 us                                                 | 780 us: 1.04x faster                                                |
| regex_dna                  | 218 ms                                                 | 211 ms: 1.04x faster                                                |
| regex_effbot               | 3.73 ms                                                | 3.62 ms: 1.03x faster                                               |
| scimark_sor                | 124 ms                                                 | 120 ms: 1.03x faster                                                |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                |
| connected_components       | 444 ms                                                 | 435 ms: 1.02x faster                                                |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                               |
| 2to3                       | 267 ms                                                 | 262 ms: 1.02x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                              |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 567 ms: 1.02x faster                                                |
| logging_simple             | 5.72 us                                                | 5.67 us: 1.01x faster                                               |
| shortest_path              | 481 ms                                                 | 478 ms: 1.01x faster                                                |
| gc_traversal               | 4.37 ms                                                | 4.36 ms: 1.00x faster                                               |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                |
| mdp                        | 2.72 sec                                               | 2.75 sec: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 551 ms: 1.01x slower                                                |
| regex_compile              | 132 ms                                                 | 134 ms: 1.01x slower                                                |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                               |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                               |
| coverage                   | 84.0 ms                                                | 85.2 ms: 1.01x slower                                               |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                                |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                               |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                |
| deltablue                  | 3.23 ms                                                | 3.29 ms: 1.02x slower                                               |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.4 ms: 1.02x slower                                               |
| async_tree_io              | 842 ms                                                 | 860 ms: 1.02x slower                                                |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                |
| typing_runtime_protocols   | 165 us                                                 | 168 us: 1.02x slower                                                |
| sqlglot_transpile          | 1.58 ms                                                | 1.63 ms: 1.03x slower                                               |
| json_dumps                 | 10.6 ms                                                | 10.9 ms: 1.03x slower                                               |
| sqlglot_optimize           | 53.7 ms                                                | 55.4 ms: 1.03x slower                                               |
| django_template            | 35.2 ms                                                | 36.2 ms: 1.03x slower                                               |
| raytrace                   | 267 ms                                                 | 276 ms: 1.03x slower                                                |
| chaos                      | 58.1 ms                                                | 60.1 ms: 1.03x slower                                               |
| html5lib                   | 64.2 ms                                                | 66.7 ms: 1.04x slower                                               |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                               |
| pickle_pure_python         | 310 us                                                 | 323 us: 1.04x slower                                                |
| async_generators           | 436 ms                                                 | 456 ms: 1.05x slower                                                |
| dulwich_log                | 64.3 ms                                                | 67.8 ms: 1.05x slower                                               |
| genshi_text                | 23.5 ms                                                | 24.8 ms: 1.05x slower                                               |
| sympy_integrate            | 19.9 ms                                                | 21.0 ms: 1.06x slower                                               |
| bench_thread_pool          | 822 us                                                 | 869 us: 1.06x slower                                                |
| sympy_sum                  | 150 ms                                                 | 159 ms: 1.06x slower                                                |
| comprehensions             | 16.5 us                                                | 17.5 us: 1.06x slower                                               |
| sympy_str                  | 275 ms                                                 | 292 ms: 1.06x slower                                                |
| sympy_expand               | 463 ms                                                 | 502 ms: 1.08x slower                                                |
| pylint                     | 313 ms                                                 | 342 ms: 1.09x slower                                                |
| sphinx                     | 1.03 sec                                               | 1.14 sec: 1.10x slower                                              |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                               |
| nqueens                    | 78.4 ms                                                | 87.1 ms: 1.11x slower                                               |
| docutils                   | 2.59 sec                                               | 2.89 sec: 1.11x slower                                              |
| async_tree_io_tg           | 857 ms                                                 | 980 ms: 1.14x slower                                                |
| genshi_xml                 | 50.9 ms                                                | 58.4 ms: 1.15x slower                                               |
| hexiom                     | 6.16 ms                                                | 7.10 ms: 1.15x slower                                               |
| generators                 | 29.0 ms                                                | 36.0 ms: 1.24x slower                                               |
| k_core                     | 2.35 sec                                               | 3.65 sec: 1.55x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 78.4 ms: 3.27x slower                                               |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (7): logging_silent, pprint_pformat, pprint_safe_repr, asyncio_websockets, async_tree_none_tg, xml_etree_iterparse, xml_etree_parse
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241111-3.14.0a1+-a2be6fd-JIT/bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd.json: sqlite_synth

- Geometric mean (including insignificant results): 1.008x faster
# HPT report

- Reliability score: 51.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x