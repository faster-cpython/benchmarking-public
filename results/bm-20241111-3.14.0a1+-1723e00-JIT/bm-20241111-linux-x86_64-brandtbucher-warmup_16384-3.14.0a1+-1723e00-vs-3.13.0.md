# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_16384
- machine: linux-x86_64
- commit hash: 1723e00
- commit date: 2024-11-11
- overall geometric mean: 1.007x faster
- HPT reliability: 59.14%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                                 |
| docutils       | 2.59 sec                                               | 2.86 sec: 1.10x slower                                               |
| html5lib       | 64.2 ms                                                | 66.5 ms: 1.04x slower                                                |
| sphinx         | 1.03 sec                                               | 1.12 sec: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 379 ms: 1.22x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                 |
| async_tree_none            | 351 ms                                                 | 334 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 586 ms: 1.02x slower                                                 |
| async_tree_io              | 842 ms                                                 | 866 ms: 1.03x slower                                                 |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 568 ms: 1.04x slower                                                 |
| async_generators           | 436 ms                                                 | 460 ms: 1.06x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 984 ms: 1.15x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.6 ms: 1.05x faster                                                |
| float          | 79.2 ms                                                | 77.1 ms: 1.03x faster                                                |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.0 ms: 1.05x faster                                                |
| regex_dna      | 218 ms                                                 | 211 ms: 1.04x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.68 ms: 1.01x faster                                                |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 194 us: 1.11x faster                                                 |
| xml_etree_generate   | 86.7 ms                                                | 79.3 ms: 1.09x faster                                                |
| xml_etree_process    | 60.6 ms                                                | 55.6 ms: 1.09x faster                                                |
| tomli_loads          | 2.14 sec                                               | 1.98 sec: 1.08x faster                                               |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 102 ms: 1.01x slower                                                 |
| pickle_pure_python   | 310 us                                                 | 324 us: 1.04x slower                                                 |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                |
| genshi_text     | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                |
| django_template | 35.2 ms                                                | 36.4 ms: 1.04x slower                                                |
| genshi_xml      | 50.9 ms                                                | 56.9 ms: 1.12x slower                                                |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 273 us: 1.31x faster                                                 |
| deepcopy_memo              | 39.1 us                                                | 30.3 us: 1.29x faster                                                |
| async_tree_memoization_tg  | 464 ms                                                 | 379 ms: 1.22x faster                                                 |
| richards                   | 48.7 ms                                                | 41.2 ms: 1.18x faster                                                |
| richards_super             | 54.9 ms                                                | 48.4 ms: 1.13x faster                                                |
| deepcopy_reduce            | 3.20 us                                                | 2.83 us: 1.13x faster                                                |
| scimark_fft                | 364 ms                                                 | 323 ms: 1.13x faster                                                 |
| go                         | 144 ms                                                 | 128 ms: 1.12x faster                                                 |
| unpickle_pure_python       | 216 us                                                 | 194 us: 1.11x faster                                                 |
| crypto_pyaes               | 75.3 ms                                                | 67.8 ms: 1.11x faster                                                |
| telco                      | 8.54 ms                                                | 7.72 ms: 1.11x faster                                                |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                |
| xml_etree_generate         | 86.7 ms                                                | 79.3 ms: 1.09x faster                                                |
| json                       | 5.36 ms                                                | 4.90 ms: 1.09x faster                                                |
| xml_etree_process          | 60.6 ms                                                | 55.6 ms: 1.09x faster                                                |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                |
| tomli_loads                | 2.14 sec                                               | 1.98 sec: 1.08x faster                                               |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.70 ms: 1.07x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.07x faster                                               |
| bpe_tokeniser              | 4.75 sec                                               | 4.49 sec: 1.06x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                 |
| nbody                      | 87.0 ms                                                | 82.6 ms: 1.05x faster                                                |
| mdp                        | 2.72 sec                                               | 2.59 sec: 1.05x faster                                               |
| fannkuch                   | 404 ms                                                 | 385 ms: 1.05x faster                                                 |
| regex_v8                   | 26.2 ms                                                | 25.0 ms: 1.05x faster                                                |
| async_tree_none            | 351 ms                                                 | 334 ms: 1.05x faster                                                 |
| pyflate                    | 471 ms                                                 | 450 ms: 1.05x faster                                                 |
| scimark_monte_carlo        | 67.4 ms                                                | 64.5 ms: 1.05x faster                                                |
| logging_format             | 6.40 us                                                | 6.13 us: 1.04x faster                                                |
| 2to3                       | 267 ms                                                 | 256 ms: 1.04x faster                                                 |
| thrift                     | 809 us                                                 | 781 us: 1.04x faster                                                 |
| regex_dna                  | 218 ms                                                 | 211 ms: 1.04x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.03x faster                                                 |
| float                      | 79.2 ms                                                | 77.1 ms: 1.03x faster                                                |
| logging_silent             | 102 ns                                                 | 99.5 ns: 1.02x faster                                                |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                |
| logging_simple             | 5.72 us                                                | 5.61 us: 1.02x faster                                                |
| scimark_sor                | 124 ms                                                 | 121 ms: 1.02x faster                                                 |
| connected_components       | 444 ms                                                 | 437 ms: 1.01x faster                                                 |
| regex_effbot               | 3.73 ms                                                | 3.68 ms: 1.01x faster                                                |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                 |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                                 |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                 |
| shortest_path              | 481 ms                                                 | 478 ms: 1.00x faster                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 102 ms: 1.01x slower                                                 |
| deltablue                  | 3.23 ms                                                | 3.27 ms: 1.01x slower                                                |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 586 ms: 1.02x slower                                                 |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                |
| dulwich_log                | 64.3 ms                                                | 65.6 ms: 1.02x slower                                                |
| typing_runtime_protocols   | 165 us                                                 | 168 us: 1.02x slower                                                 |
| sympy_str                  | 275 ms                                                 | 281 ms: 1.02x slower                                                 |
| sqlglot_transpile          | 1.58 ms                                                | 1.63 ms: 1.03x slower                                                |
| coverage                   | 84.0 ms                                                | 86.2 ms: 1.03x slower                                                |
| pprint_safe_repr           | 728 ms                                                 | 749 ms: 1.03x slower                                                 |
| async_tree_io              | 842 ms                                                 | 866 ms: 1.03x slower                                                 |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                |
| scimark_lu                 | 113 ms                                                 | 116 ms: 1.03x slower                                                 |
| genshi_text                | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                                 |
| sqlglot_optimize           | 53.7 ms                                                | 55.5 ms: 1.03x slower                                                |
| gc_traversal               | 4.37 ms                                                | 4.52 ms: 1.03x slower                                                |
| chaos                      | 58.1 ms                                                | 60.1 ms: 1.04x slower                                                |
| django_template            | 35.2 ms                                                | 36.4 ms: 1.04x slower                                                |
| html5lib                   | 64.2 ms                                                | 66.5 ms: 1.04x slower                                                |
| pprint_pformat             | 1.49 sec                                               | 1.55 sec: 1.04x slower                                               |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 20.7 ms: 1.04x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 568 ms: 1.04x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.04x slower                                                 |
| pickle_pure_python         | 310 us                                                 | 324 us: 1.04x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                |
| raytrace                   | 267 ms                                                 | 280 ms: 1.05x slower                                                 |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.06x slower                                                |
| async_generators           | 436 ms                                                 | 460 ms: 1.06x slower                                                 |
| bench_thread_pool          | 822 us                                                 | 876 us: 1.07x slower                                                 |
| sympy_expand               | 463 ms                                                 | 498 ms: 1.07x slower                                                 |
| sphinx                     | 1.03 sec                                               | 1.12 sec: 1.09x slower                                               |
| docutils                   | 2.59 sec                                               | 2.86 sec: 1.10x slower                                               |
| create_gc_cycles           | 2.41 ms                                                | 2.66 ms: 1.11x slower                                                |
| genshi_xml                 | 50.9 ms                                                | 56.9 ms: 1.12x slower                                                |
| hexiom                     | 6.16 ms                                                | 6.98 ms: 1.13x slower                                                |
| nqueens                    | 78.4 ms                                                | 89.2 ms: 1.14x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 984 ms: 1.15x slower                                                 |
| generators                 | 29.0 ms                                                | 35.8 ms: 1.24x slower                                                |
| k_core                     | 2.35 sec                                               | 3.61 sec: 1.54x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 78.3 ms: 3.26x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (5): xml_etree_parse, sqlalchemy_imperative, asyncio_websockets, async_tree_none_tg, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241111-3.14.0a1+-1723e00-JIT/bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00.json: sqlite_synth

- Geometric mean (including insignificant results): 1.007x faster
# HPT report

- Reliability score: 59.14% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x