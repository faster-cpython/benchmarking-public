# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_65536
- machine: linux-x86_64
- commit hash: c17f578
- commit date: 2024-11-12
- overall geometric mean: 1.006x faster
- HPT reliability: 50.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 258 ms: 1.03x faster                                                 |
| docutils       | 2.59 sec                                               | 2.81 sec: 1.08x slower                                               |
| html5lib       | 64.2 ms                                                | 66.4 ms: 1.03x slower                                                |
| sphinx         | 1.03 sec                                               | 1.10 sec: 1.06x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 378 ms: 1.23x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                                 |
| async_tree_none            | 351 ms                                                 | 332 ms: 1.06x faster                                                 |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                |
| async_tree_io              | 842 ms                                                 | 868 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 564 ms: 1.03x slower                                                 |
| async_generators           | 436 ms                                                 | 462 ms: 1.06x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 979 ms: 1.14x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.5 ms: 1.05x faster                                                |
| float          | 79.2 ms                                                | 77.1 ms: 1.03x faster                                                |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.74 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 78.7 ms: 1.10x faster                                                |
| xml_etree_process    | 60.6 ms                                                | 55.2 ms: 1.10x faster                                                |
| tomli_loads          | 2.14 sec                                               | 1.98 sec: 1.08x faster                                               |
| unpickle_pure_python | 216 us                                                 | 200 us: 1.08x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.02x slower                                                 |
| pickle_pure_python   | 310 us                                                 | 318 us: 1.03x slower                                                 |
| xml_etree_parse      | 156 ms                                                 | 160 ms: 1.03x slower                                                 |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                |
| django_template | 35.2 ms                                                | 36.1 ms: 1.03x slower                                                |
| genshi_text     | 23.5 ms                                                | 24.2 ms: 1.03x slower                                                |
| genshi_xml      | 50.9 ms                                                | 57.2 ms: 1.12x slower                                                |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.4 us: 1.33x faster                                                |
| deepcopy                   | 358 us                                                 | 272 us: 1.32x faster                                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 378 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.20 us                                                | 2.75 us: 1.17x faster                                                |
| go                         | 144 ms                                                 | 127 ms: 1.13x faster                                                 |
| scimark_fft                | 364 ms                                                 | 326 ms: 1.12x faster                                                 |
| xml_etree_generate         | 86.7 ms                                                | 78.7 ms: 1.10x faster                                                |
| xml_etree_process          | 60.6 ms                                                | 55.2 ms: 1.10x faster                                                |
| telco                      | 8.54 ms                                                | 7.80 ms: 1.10x faster                                                |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                |
| crypto_pyaes               | 75.3 ms                                                | 69.0 ms: 1.09x faster                                                |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.63 ms: 1.09x faster                                                |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                |
| tomli_loads                | 2.14 sec                                               | 1.98 sec: 1.08x faster                                               |
| json                       | 5.36 ms                                                | 4.97 ms: 1.08x faster                                                |
| unpickle_pure_python       | 216 us                                                 | 200 us: 1.08x faster                                                 |
| richards                   | 48.7 ms                                                | 45.2 ms: 1.08x faster                                                |
| mdp                        | 2.72 sec                                               | 2.55 sec: 1.07x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                                 |
| async_tree_none            | 351 ms                                                 | 332 ms: 1.06x faster                                                 |
| bpe_tokeniser              | 4.75 sec                                               | 4.50 sec: 1.05x faster                                               |
| nbody                      | 87.0 ms                                                | 82.5 ms: 1.05x faster                                                |
| fannkuch                   | 404 ms                                                 | 385 ms: 1.05x faster                                                 |
| richards_super             | 54.9 ms                                                | 52.4 ms: 1.05x faster                                                |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.04x faster                                                 |
| scimark_monte_carlo        | 67.4 ms                                                | 65.2 ms: 1.03x faster                                                |
| 2to3                       | 267 ms                                                 | 258 ms: 1.03x faster                                                 |
| logging_silent             | 102 ns                                                 | 98.7 ns: 1.03x faster                                                |
| scimark_sor                | 124 ms                                                 | 120 ms: 1.03x faster                                                 |
| float                      | 79.2 ms                                                | 77.1 ms: 1.03x faster                                                |
| thrift                     | 809 us                                                 | 788 us: 1.03x faster                                                 |
| pprint_pformat             | 1.49 sec                                               | 1.46 sec: 1.02x faster                                               |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                 |
| pprint_safe_repr           | 728 ms                                                 | 715 ms: 1.02x faster                                                 |
| logging_format             | 6.40 us                                                | 6.30 us: 1.02x faster                                                |
| pyflate                    | 471 ms                                                 | 464 ms: 1.02x faster                                                 |
| connected_components       | 444 ms                                                 | 438 ms: 1.01x faster                                                 |
| deltablue                  | 3.23 ms                                                | 3.19 ms: 1.01x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                               |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| regex_effbot               | 3.73 ms                                                | 3.74 ms: 1.00x slower                                                |
| sqlglot_transpile          | 1.58 ms                                                | 1.59 ms: 1.00x slower                                                |
| scimark_lu                 | 113 ms                                                 | 113 ms: 1.00x slower                                                 |
| sympy_expand               | 463 ms                                                 | 467 ms: 1.01x slower                                                 |
| sqlglot_optimize           | 53.7 ms                                                | 54.2 ms: 1.01x slower                                                |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.01x slower                                                |
| meteor_contest             | 109 ms                                                 | 111 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 165 us                                                 | 168 us: 1.02x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.09 ms: 1.02x slower                                                |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.02x slower                                                 |
| dulwich_log                | 64.3 ms                                                | 65.7 ms: 1.02x slower                                                |
| raytrace                   | 267 ms                                                 | 273 ms: 1.02x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 20.4 ms: 1.02x slower                                                |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.02x slower                                                |
| pickle_pure_python         | 310 us                                                 | 318 us: 1.03x slower                                                 |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.5 ms: 1.03x slower                                                |
| django_template            | 35.2 ms                                                | 36.1 ms: 1.03x slower                                                |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                 |
| xml_etree_parse            | 156 ms                                                 | 160 ms: 1.03x slower                                                 |
| genshi_text                | 23.5 ms                                                | 24.2 ms: 1.03x slower                                                |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                |
| async_tree_io              | 842 ms                                                 | 868 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 564 ms: 1.03x slower                                                 |
| chaos                      | 58.1 ms                                                | 60.0 ms: 1.03x slower                                                |
| html5lib                   | 64.2 ms                                                | 66.4 ms: 1.03x slower                                                |
| spectral_norm              | 115 ms                                                 | 120 ms: 1.04x slower                                                 |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.05x slower                                                |
| bench_thread_pool          | 822 us                                                 | 869 us: 1.06x slower                                                 |
| async_generators           | 436 ms                                                 | 462 ms: 1.06x slower                                                 |
| sphinx                     | 1.03 sec                                               | 1.10 sec: 1.06x slower                                               |
| docutils                   | 2.59 sec                                               | 2.81 sec: 1.08x slower                                               |
| hexiom                     | 6.16 ms                                                | 6.71 ms: 1.09x slower                                                |
| gc_traversal               | 4.37 ms                                                | 4.80 ms: 1.10x slower                                                |
| create_gc_cycles           | 2.41 ms                                                | 2.70 ms: 1.12x slower                                                |
| genshi_xml                 | 50.9 ms                                                | 57.2 ms: 1.12x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 979 ms: 1.14x slower                                                 |
| nqueens                    | 78.4 ms                                                | 90.5 ms: 1.15x slower                                                |
| generators                 | 29.0 ms                                                | 36.4 ms: 1.26x slower                                                |
| k_core                     | 2.35 sec                                               | 3.64 sec: 1.55x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 79.2 ms: 3.30x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (10): json_loads, regex_dna, logging_simple, coverage, sympy_str, asyncio_websockets, shortest_path, async_tree_cpu_io_mixed, async_tree_none_tg, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241112-3.14.0a1+-c17f578-JIT/bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578.json: sqlite_synth

- Geometric mean (including insignificant results): 1.006x faster
# HPT report

- Reliability score: 50.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x