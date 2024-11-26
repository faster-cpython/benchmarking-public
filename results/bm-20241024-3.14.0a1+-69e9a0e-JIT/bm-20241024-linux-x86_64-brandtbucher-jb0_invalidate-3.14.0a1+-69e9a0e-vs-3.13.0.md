# Results vs. 3.13.0

- fork: brandtbucher
- ref: jb0_invalidate
- machine: linux-x86_64
- commit hash: 69e9a0e
- commit date: 2024-10-24
- overall geometric mean: 1.048x slower
- HPT reliability: 99.69%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 284 ms: 1.07x slower                                                   |
| docutils       | 2.59 sec                                               | 3.36 sec: 1.29x slower                                                 |
| html5lib       | 64.2 ms                                                | 69.9 ms: 1.09x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.32 sec: 1.28x slower                                                 |
| tornado_http   | 92.4 ms                                                | 112 ms: 1.21x slower                                                   |
| Geometric mean | (ref)                                                  | 1.18x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 407 ms: 1.14x faster                                                   |
| asyncio_websockets         | 552 ms                                                 | 559 ms: 1.01x slower                                                   |
| async_tree_none_tg         | 321 ms                                                 | 332 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 599 ms: 1.04x slower                                                   |
| async_generators           | 436 ms                                                 | 462 ms: 1.06x slower                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 589 ms: 1.08x slower                                                   |
| async_tree_io_tg           | 857 ms                                                 | 953 ms: 1.11x slower                                                   |
| async_tree_io              | 842 ms                                                 | 950 ms: 1.13x slower                                                   |
| coroutines                 | 22.7 ms                                                | 26.5 ms: 1.17x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                           |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.4 ms: 1.06x faster                                                  |
| float          | 79.2 ms                                                | 75.3 ms: 1.05x faster                                                  |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                  |
| regex_dna      | 218 ms                                                 | 220 ms: 1.01x slower                                                   |
| regex_compile  | 132 ms                                                 | 147 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.99 sec: 1.08x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                   |
| pickle_pure_python   | 310 us                                                 | 295 us: 1.05x faster                                                   |
| xml_etree_generate   | 86.7 ms                                                | 83.2 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 99.4 ms: 1.02x faster                                                  |
| xml_etree_process    | 60.6 ms                                                | 59.8 ms: 1.01x faster                                                  |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                                  |
| unpickle_pure_python | 216 us                                                 | 225 us: 1.04x slower                                                   |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.9 ms: 1.05x faster                                                  |
| python_startup_no_site | 6.96 ms                                                | 7.22 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.6 ms: 1.05x faster                                                  |
| genshi_text     | 23.5 ms                                                | 26.2 ms: 1.11x slower                                                  |
| django_template | 35.2 ms                                                | 40.1 ms: 1.14x slower                                                  |
| genshi_xml      | 50.9 ms                                                | 62.9 ms: 1.23x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.11x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 275 us: 1.30x faster                                                   |
| deepcopy_memo              | 39.1 us                                                | 30.2 us: 1.30x faster                                                  |
| scimark_fft                | 364 ms                                                 | 319 ms: 1.14x faster                                                   |
| async_tree_memoization_tg  | 464 ms                                                 | 407 ms: 1.14x faster                                                   |
| telco                      | 8.54 ms                                                | 7.62 ms: 1.12x faster                                                  |
| go                         | 144 ms                                                 | 129 ms: 1.11x faster                                                   |
| deepcopy_reduce            | 3.20 us                                                | 2.87 us: 1.11x faster                                                  |
| crypto_pyaes               | 75.3 ms                                                | 69.1 ms: 1.09x faster                                                  |
| scimark_monte_carlo        | 67.4 ms                                                | 62.4 ms: 1.08x faster                                                  |
| tomli_loads                | 2.14 sec                                               | 1.99 sec: 1.08x faster                                                 |
| fannkuch                   | 404 ms                                                 | 378 ms: 1.07x faster                                                   |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.73 ms: 1.07x faster                                                  |
| json                       | 5.36 ms                                                | 5.08 ms: 1.06x faster                                                  |
| bpe_tokeniser              | 4.75 sec                                               | 4.50 sec: 1.06x faster                                                 |
| nbody                      | 87.0 ms                                                | 82.4 ms: 1.06x faster                                                  |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                   |
| pickle_pure_python         | 310 us                                                 | 295 us: 1.05x faster                                                   |
| float                      | 79.2 ms                                                | 75.3 ms: 1.05x faster                                                  |
| python_startup             | 12.5 ms                                                | 11.9 ms: 1.05x faster                                                  |
| mako                       | 11.1 ms                                                | 10.6 ms: 1.05x faster                                                  |
| pathlib                    | 17.5 ms                                                | 16.8 ms: 1.05x faster                                                  |
| xml_etree_generate         | 86.7 ms                                                | 83.2 ms: 1.04x faster                                                  |
| regex_v8                   | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 99.4 ms: 1.02x faster                                                  |
| scimark_sor                | 124 ms                                                 | 121 ms: 1.02x faster                                                   |
| xml_etree_process          | 60.6 ms                                                | 59.8 ms: 1.01x faster                                                  |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                   |
| pyflate                    | 471 ms                                                 | 466 ms: 1.01x faster                                                   |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                                  |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.00x slower                                                   |
| scimark_lu                 | 113 ms                                                 | 113 ms: 1.00x slower                                                   |
| regex_dna                  | 218 ms                                                 | 220 ms: 1.01x slower                                                   |
| richards_super             | 54.9 ms                                                | 55.4 ms: 1.01x slower                                                  |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| asyncio_websockets         | 552 ms                                                 | 559 ms: 1.01x slower                                                   |
| richards                   | 48.7 ms                                                | 49.6 ms: 1.02x slower                                                  |
| chaos                      | 58.1 ms                                                | 59.4 ms: 1.02x slower                                                  |
| thrift                     | 809 us                                                 | 829 us: 1.02x slower                                                   |
| mdp                        | 2.72 sec                                               | 2.81 sec: 1.03x slower                                                 |
| coverage                   | 84.0 ms                                                | 86.9 ms: 1.03x slower                                                  |
| async_tree_none_tg         | 321 ms                                                 | 332 ms: 1.04x slower                                                   |
| python_startup_no_site     | 6.96 ms                                                | 7.22 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 599 ms: 1.04x slower                                                   |
| unpickle_pure_python       | 216 us                                                 | 225 us: 1.04x slower                                                   |
| gc_traversal               | 4.37 ms                                                | 4.55 ms: 1.04x slower                                                  |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.06x slower                                                  |
| async_generators           | 436 ms                                                 | 462 ms: 1.06x slower                                                   |
| 2to3                       | 267 ms                                                 | 284 ms: 1.07x slower                                                   |
| dulwich_log                | 64.3 ms                                                | 68.7 ms: 1.07x slower                                                  |
| logging_silent             | 102 ns                                                 | 109 ns: 1.07x slower                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 589 ms: 1.08x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.9 us: 1.08x slower                                                  |
| pycparser                  | 1.20 sec                                               | 1.31 sec: 1.09x slower                                                 |
| html5lib                   | 64.2 ms                                                | 69.9 ms: 1.09x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 119 ms: 1.10x slower                                                   |
| async_tree_io_tg           | 857 ms                                                 | 953 ms: 1.11x slower                                                   |
| genshi_text                | 23.5 ms                                                | 26.2 ms: 1.11x slower                                                  |
| regex_compile              | 132 ms                                                 | 147 ms: 1.11x slower                                                   |
| create_gc_cycles           | 2.41 ms                                                | 2.69 ms: 1.12x slower                                                  |
| raytrace                   | 267 ms                                                 | 299 ms: 1.12x slower                                                   |
| sqlglot_parse              | 1.27 ms                                                | 1.43 ms: 1.12x slower                                                  |
| async_tree_io              | 842 ms                                                 | 950 ms: 1.13x slower                                                   |
| nqueens                    | 78.4 ms                                                | 89.3 ms: 1.14x slower                                                  |
| django_template            | 35.2 ms                                                | 40.1 ms: 1.14x slower                                                  |
| sympy_expand               | 463 ms                                                 | 536 ms: 1.16x slower                                                   |
| hexiom                     | 6.16 ms                                                | 7.17 ms: 1.16x slower                                                  |
| coroutines                 | 22.7 ms                                                | 26.5 ms: 1.17x slower                                                  |
| sqlglot_transpile          | 1.58 ms                                                | 1.85 ms: 1.17x slower                                                  |
| bench_thread_pool          | 822 us                                                 | 967 us: 1.18x slower                                                   |
| logging_format             | 6.40 us                                                | 7.61 us: 1.19x slower                                                  |
| sqlglot_optimize           | 53.7 ms                                                | 65.1 ms: 1.21x slower                                                  |
| tornado_http               | 92.4 ms                                                | 112 ms: 1.21x slower                                                   |
| sympy_str                  | 275 ms                                                 | 335 ms: 1.22x slower                                                   |
| logging_simple             | 5.72 us                                                | 7.01 us: 1.23x slower                                                  |
| genshi_xml                 | 50.9 ms                                                | 62.9 ms: 1.23x slower                                                  |
| deltablue                  | 3.23 ms                                                | 4.04 ms: 1.25x slower                                                  |
| generators                 | 29.0 ms                                                | 36.7 ms: 1.27x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.32 sec: 1.28x slower                                                 |
| docutils                   | 2.59 sec                                               | 3.36 sec: 1.29x slower                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 174 ms: 1.30x slower                                                   |
| sqlalchemy_imperative      | 17.1 ms                                                | 22.7 ms: 1.33x slower                                                  |
| sympy_integrate            | 19.9 ms                                                | 26.5 ms: 1.33x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 209 ms: 1.39x slower                                                   |
| pylint                     | 313 ms                                                 | 460 ms: 1.47x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 89.3 ms: 3.72x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x slower                                                           |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_none, pprint_safe_repr, regex_effbot, typing_runtime_protocols, pprint_pformat
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.048x slower
# HPT report

- Reliability score: 99.69% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x