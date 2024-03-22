# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_ghccc
- machine: darwin-arm64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.02x faster
- HPT reliability: 99.72%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.60x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 192 ms: 1.00x slower                                                 |
| chameleon      | 6.26 ms                                                | 4.48 ms: 1.40x faster                                                |
| docutils       | 1.73 sec                                               | 2.61 sec: 1.51x slower                                               |
| html5lib       | 42.4 ms                                                | 38.0 ms: 1.11x faster                                                |
| tornado_http   | 86.7 ms                                                | 78.3 ms: 1.11x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 649 ms                                                 | 2.81 sec: 4.32x slower                                               |
| async_tree_none         | 388 ms                                                 | 2.21 sec: 5.68x slower                                               |
| async_tree_memoization  | 474 ms                                                 | 2.83 sec: 5.97x slower                                               |
| async_tree_io           | 980 ms                                                 | 8.95 sec: 9.13x slower                                               |
| Geometric mean          | (ref)                                                  | 6.05x slower                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 72.4 ms: 1.28x faster                                                |
| float          | 69.0 ms                                                | 89.7 ms: 1.30x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 152 ms: 1.15x faster                                                 |
| regex_compile  | 95.3 ms                                                | 83.2 ms: 1.14x faster                                                |
| regex_v8       | 17.1 ms                                                | 17.2 ms: 1.00x slower                                                |
| regex_effbot   | 2.46 ms                                                | 2.62 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 185 us: 1.52x faster                                                 |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.30 sec: 1.31x faster                                               |
| json_dumps           | 8.11 ms                                                | 6.39 ms: 1.27x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 41.3 ms: 1.13x faster                                                |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                |
| unpickle             | 8.80 us                                                | 9.33 us: 1.06x slower                                                |
| pickle               | 6.97 us                                                | 7.41 us: 1.06x slower                                                |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                                |
| pickle_list          | 2.74 us                                                | 3.01 us: 1.10x slower                                                |
| xml_etree_generate   | 53.5 ms                                                | 61.0 ms: 1.14x slower                                                |
| unpickle_list        | 2.69 us                                                | 3.08 us: 1.14x slower                                                |
| xml_etree_parse      | 108 ms                                                 | 131 ms: 1.21x slower                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 105 ms: 1.46x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.9 ms: 1.74x slower                                                |
| python_startup_no_site | 7.91 ms                                                | 17.2 ms: 2.18x slower                                                |
| Geometric mean         | (ref)                                                  | 1.95x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.91 ms: 1.43x faster                                                |
| django_template | 26.4 ms                                                | 20.4 ms: 1.29x faster                                                |
| genshi_text     | 17.3 ms                                                | 14.8 ms: 1.17x faster                                                |
| genshi_xml      | 33.8 ms                                                | 35.4 ms: 1.05x slower                                                |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 69.6 us: 4.64x faster                                                |
| deltablue                | 4.91 ms                                                | 2.46 ms: 1.99x faster                                                |
| logging_silent           | 117 ns                                                 | 65.6 ns: 1.79x faster                                                |
| chaos                    | 65.8 ms                                                | 38.3 ms: 1.72x faster                                                |
| richards_super           | 57.8 ms                                                | 34.8 ms: 1.66x faster                                                |
| raytrace                 | 301 ms                                                 | 186 ms: 1.62x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 409 ms: 1.61x faster                                                 |
| richards                 | 48.7 ms                                                | 31.8 ms: 1.53x faster                                                |
| crypto_pyaes             | 71.8 ms                                                | 47.1 ms: 1.53x faster                                                |
| pickle_pure_python       | 281 us                                                 | 185 us: 1.52x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 820 us: 1.52x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 45.0 ms: 1.46x faster                                                |
| sqlglot_transpile        | 1.44 ms                                                | 1.01 ms: 1.43x faster                                                |
| go                       | 151 ms                                                 | 105 ms: 1.43x faster                                                 |
| mako                     | 9.87 ms                                                | 6.91 ms: 1.43x faster                                                |
| deepcopy_memo            | 34.7 us                                                | 24.4 us: 1.42x faster                                                |
| chameleon                | 6.26 ms                                                | 4.48 ms: 1.40x faster                                                |
| comprehensions           | 16.9 us                                                | 12.3 us: 1.38x faster                                                |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.30 us: 1.35x faster                                                |
| logging_format           | 4.83 us                                                | 3.58 us: 1.35x faster                                                |
| tomli_loads              | 1.71 sec                                               | 1.30 sec: 1.31x faster                                               |
| thrift                   | 572 us                                                 | 437 us: 1.31x faster                                                 |
| django_template          | 26.4 ms                                                | 20.4 ms: 1.29x faster                                                |
| pprint_safe_repr         | 641 ms                                                 | 496 ms: 1.29x faster                                                 |
| nbody                    | 93.0 ms                                                | 72.4 ms: 1.28x faster                                                |
| hexiom                   | 6.19 ms                                                | 4.85 ms: 1.28x faster                                                |
| pprint_pformat           | 1.30 sec                                               | 1.02 sec: 1.27x faster                                               |
| json_dumps               | 8.11 ms                                                | 6.39 ms: 1.27x faster                                                |
| pyflate                  | 427 ms                                                 | 336 ms: 1.27x faster                                                 |
| scimark_lu               | 103 ms                                                 | 81.5 ms: 1.26x faster                                                |
| deepcopy                 | 272 us                                                 | 217 us: 1.25x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.88 us: 1.24x faster                                                |
| sympy_sum                | 92.2 ms                                                | 74.5 ms: 1.24x faster                                                |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.31 sec: 1.23x faster                                               |
| scimark_sor              | 128 ms                                                 | 106 ms: 1.20x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 11.0 ms: 1.20x faster                                                |
| sympy_str                | 165 ms                                                 | 138 ms: 1.19x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 79.8 ms: 1.19x faster                                                |
| dulwich_log              | 35.3 ms                                                | 29.8 ms: 1.19x faster                                                |
| generators               | 32.3 ms                                                | 27.3 ms: 1.18x faster                                                |
| genshi_text              | 17.3 ms                                                | 14.8 ms: 1.17x faster                                                |
| coroutines               | 20.7 ms                                                | 18.0 ms: 1.15x faster                                                |
| regex_dna                | 174 ms                                                 | 152 ms: 1.15x faster                                                 |
| regex_compile            | 95.3 ms                                                | 83.2 ms: 1.14x faster                                                |
| fannkuch                 | 303 ms                                                 | 266 ms: 1.14x faster                                                 |
| mypy2                    | 607 ms                                                 | 533 ms: 1.14x faster                                                 |
| create_gc_cycles         | 860 us                                                 | 760 us: 1.13x faster                                                 |
| sympy_expand             | 269 ms                                                 | 238 ms: 1.13x faster                                                 |
| scimark_fft              | 224 ms                                                 | 199 ms: 1.13x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 41.3 ms: 1.13x faster                                                |
| html5lib                 | 42.4 ms                                                | 38.0 ms: 1.11x faster                                                |
| tornado_http             | 86.7 ms                                                | 78.3 ms: 1.11x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 174 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.16 ms: 1.08x faster                                                |
| bench_thread_pool        | 527 us                                                 | 493 us: 1.07x faster                                                 |
| gunicorn                 | 1.30 ms                                                | 1.22 ms: 1.07x faster                                                |
| sqlglot_optimize         | 36.8 ms                                                | 34.7 ms: 1.06x faster                                                |
| aiohttp                  | 1.22 ms                                                | 1.16 ms: 1.06x faster                                                |
| pycparser                | 877 ms                                                 | 834 ms: 1.05x faster                                                 |
| json                     | 3.08 ms                                                | 2.96 ms: 1.04x faster                                                |
| meteor_contest           | 77.7 ms                                                | 75.0 ms: 1.04x faster                                                |
| nqueens                  | 63.8 ms                                                | 61.6 ms: 1.04x faster                                                |
| mdp                      | 1.63 sec                                               | 1.61 sec: 1.01x faster                                               |
| regex_v8                 | 17.1 ms                                                | 17.2 ms: 1.00x slower                                                |
| 2to3                     | 192 ms                                                 | 192 ms: 1.00x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.44 ms: 1.03x slower                                                |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                |
| genshi_xml               | 33.8 ms                                                | 35.4 ms: 1.05x slower                                                |
| unpickle                 | 8.80 us                                                | 9.33 us: 1.06x slower                                                |
| pickle                   | 6.97 us                                                | 7.41 us: 1.06x slower                                                |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                                |
| regex_effbot             | 2.46 ms                                                | 2.62 ms: 1.07x slower                                                |
| sqlite_synth             | 1.46 us                                                | 1.60 us: 1.10x slower                                                |
| pickle_list              | 2.74 us                                                | 3.01 us: 1.10x slower                                                |
| coverage                 | 41.5 ms                                                | 46.8 ms: 1.13x slower                                                |
| xml_etree_generate       | 53.5 ms                                                | 61.0 ms: 1.14x slower                                                |
| unpickle_list            | 2.69 us                                                | 3.08 us: 1.14x slower                                                |
| xml_etree_parse          | 108 ms                                                 | 131 ms: 1.21x slower                                                 |
| float                    | 69.0 ms                                                | 89.7 ms: 1.30x slower                                                |
| telco                    | 3.49 ms                                                | 4.54 ms: 1.30x slower                                                |
| xml_etree_iterparse      | 72.1 ms                                                | 105 ms: 1.46x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 54.8 ms: 1.47x slower                                                |
| async_generators         | 231 ms                                                 | 345 ms: 1.49x slower                                                 |
| docutils                 | 1.73 sec                                               | 2.61 sec: 1.51x slower                                               |
| python_startup           | 10.9 ms                                                | 18.9 ms: 1.74x slower                                                |
| dask                     | 253 ms                                                 | 453 ms: 1.79x slower                                                 |
| pylint                   | 277 ms                                                 | 587 ms: 2.12x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 17.2 ms: 2.18x slower                                                |
| unpack_sequence          | 39.0 ns                                                | 113 ns: 2.89x slower                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 2.81 sec: 4.32x slower                                               |
| async_tree_none          | 388 ms                                                 | 2.21 sec: 5.68x slower                                               |
| async_tree_memoization   | 474 ms                                                 | 2.83 sec: 5.97x slower                                               |
| async_tree_io            | 980 ms                                                 | 8.95 sec: 9.13x slower                                               |
| Geometric mean           | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (3): asyncio_websockets, pidigits, pathlib
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240321-3.13.0a5+-98575b4-JIT/bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 99.72% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.01x


# Memory

- memory change: 1.60x