# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact
- machine: darwin-arm64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 176 ms: 1.09x faster                                                  |
| docutils       | 1.73 sec                                               | 1.55 sec: 1.12x faster                                                |
| html5lib       | 42.4 ms                                                | 32.1 ms: 1.32x faster                                                 |
| tornado_http   | 86.7 ms                                                | 69.5 ms: 1.25x faster                                                 |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 228 ms: 1.70x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 282 ms: 1.68x faster                                                  |
| async_tree_io           | 980 ms                                                 | 597 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 489 ms: 1.33x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.58x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.3 ms: 1.47x faster                                                 |
| float          | 69.0 ms                                                | 47.4 ms: 1.46x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.1 ms: 1.29x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.02x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 181 us: 1.55x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 140 us: 1.39x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.29 sec: 1.32x faster                                                |
| json_dumps           | 8.11 ms                                                | 6.32 ms: 1.28x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.7 ms: 1.23x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| json_loads           | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.91 us: 1.08x slower                                                 |
| unpickle             | 8.80 us                                                | 9.51 us: 1.08x slower                                                 |
| pickle               | 6.97 us                                                | 7.55 us: 1.08x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.98 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.4 ms: 1.51x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.6 ms: 1.72x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.61x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.51 ms: 1.52x faster                                                 |
| django_template | 26.4 ms                                                | 23.1 ms: 1.14x faster                                                 |
| genshi_text     | 17.3 ms                                                | 16.5 ms: 1.05x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 36.8 ms: 1.09x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 98.8 us: 3.27x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 17.0 us: 2.05x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.57 ms: 1.91x faster                                                 |
| logging_silent           | 117 ns                                                 | 65.4 ns: 1.79x faster                                                 |
| deepcopy                 | 272 us                                                 | 158 us: 1.72x faster                                                  |
| async_tree_none          | 388 ms                                                 | 228 ms: 1.70x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 282 ms: 1.68x faster                                                  |
| raytrace                 | 301 ms                                                 | 182 ms: 1.66x faster                                                  |
| async_tree_io            | 980 ms                                                 | 597 ms: 1.64x faster                                                  |
| chaos                    | 65.8 ms                                                | 41.5 ms: 1.59x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 181 us: 1.55x faster                                                  |
| mako                     | 9.87 ms                                                | 6.51 ms: 1.52x faster                                                 |
| richards_super           | 57.8 ms                                                | 38.5 ms: 1.50x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 443 ms: 1.49x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 44.5 ms: 1.47x faster                                                 |
| pylint                   | 277 ms                                                 | 188 ms: 1.47x faster                                                  |
| nbody                    | 93.0 ms                                                | 63.3 ms: 1.47x faster                                                 |
| float                    | 69.0 ms                                                | 47.4 ms: 1.46x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.62 us: 1.44x faster                                                 |
| richards                 | 48.7 ms                                                | 33.9 ms: 1.43x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 871 us: 1.43x faster                                                  |
| go                       | 151 ms                                                 | 106 ms: 1.43x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 67.1 ms: 1.41x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.41 ms: 1.40x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 140 us: 1.39x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.05 ms: 1.38x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 52.5 ms: 1.37x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.26 us: 1.37x faster                                                 |
| logging_format           | 4.83 us                                                | 3.55 us: 1.36x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.5 us: 1.36x faster                                                 |
| pyflate                  | 427 ms                                                 | 318 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 489 ms: 1.33x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.29 sec: 1.32x faster                                                |
| pprint_safe_repr         | 641 ms                                                 | 485 ms: 1.32x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 988 ms: 1.32x faster                                                  |
| html5lib                 | 42.4 ms                                                | 32.1 ms: 1.32x faster                                                 |
| regex_compile            | 95.3 ms                                                | 74.1 ms: 1.29x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.32 ms: 1.28x faster                                                 |
| pycparser                | 877 ms                                                 | 687 ms: 1.28x faster                                                  |
| tornado_http             | 86.7 ms                                                | 69.5 ms: 1.25x faster                                                 |
| fannkuch                 | 303 ms                                                 | 243 ms: 1.24x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                |
| thrift                   | 572 us                                                 | 462 us: 1.24x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 37.7 ms: 1.23x faster                                                 |
| generators               | 32.3 ms                                                | 26.3 ms: 1.23x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 75.4 ms: 1.22x faster                                                 |
| scimark_fft              | 224 ms                                                 | 187 ms: 1.20x faster                                                  |
| scimark_sor              | 128 ms                                                 | 107 ms: 1.19x faster                                                  |
| scimark_lu               | 103 ms                                                 | 86.3 ms: 1.19x faster                                                 |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.4 ms: 1.16x faster                                                 |
| sympy_str                | 165 ms                                                 | 145 ms: 1.14x faster                                                  |
| django_template          | 26.4 ms                                                | 23.1 ms: 1.14x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.00 ms: 1.14x faster                                                 |
| coroutines               | 20.7 ms                                                | 18.3 ms: 1.13x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.55 sec: 1.12x faster                                                |
| dask                     | 253 ms                                                 | 231 ms: 1.10x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.49 sec: 1.09x faster                                                |
| 2to3                     | 192 ms                                                 | 176 ms: 1.09x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 489 us: 1.08x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 72.7 ms: 1.07x faster                                                 |
| sympy_expand             | 269 ms                                                 | 252 ms: 1.07x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 34.5 ms: 1.06x faster                                                 |
| nqueens                  | 63.8 ms                                                | 60.0 ms: 1.06x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.1 ms: 1.06x faster                                                 |
| genshi_text              | 17.3 ms                                                | 16.5 ms: 1.05x faster                                                 |
| json                     | 3.08 ms                                                | 2.94 ms: 1.05x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.02x slower                                                 |
| json_loads               | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 912 us: 1.06x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.91 us: 1.08x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.51 us: 1.08x slower                                                 |
| pickle                   | 6.97 us                                                | 7.55 us: 1.08x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.58 us: 1.08x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.98 us: 1.09x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 36.8 ms: 1.09x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.61 ms: 1.11x slower                                                 |
| coverage                 | 41.5 ms                                                | 48.0 ms: 1.16x slower                                                 |
| async_generators         | 231 ms                                                 | 306 ms: 1.32x slower                                                  |
| telco                    | 3.49 ms                                                | 4.63 ms: 1.33x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 51.5 ms: 1.38x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.4 ms: 1.51x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.6 ms: 1.72x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, xml_etree_generate, xml_etree_iterparse
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (13) of results/bm-20240619-3.14.0a0-e04d5ab-JIT/bm-20240619-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.41x