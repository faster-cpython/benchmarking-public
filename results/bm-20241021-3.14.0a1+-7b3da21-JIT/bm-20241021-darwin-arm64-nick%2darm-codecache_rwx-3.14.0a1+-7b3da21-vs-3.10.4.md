# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache_rwx
- machine: darwin-arm64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.279x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 171 ms: 1.12x faster                                                |
| docutils       | 1.73 sec                                               | 1.49 sec: 1.16x faster                                              |
| html5lib       | 42.4 ms                                                | 31.1 ms: 1.36x faster                                               |
| tornado_http   | 86.7 ms                                                | 74.1 ms: 1.17x faster                                               |
| Geometric mean | (ref)                                                  | 1.20x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 198 ms: 1.96x faster                                                |
| async_tree_memoization  | 474 ms                                                 | 262 ms: 1.80x faster                                                |
| async_tree_io           | 980 ms                                                 | 580 ms: 1.69x faster                                                |
| async_tree_cpu_io_mixed | 649 ms                                                 | 455 ms: 1.43x faster                                                |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 48.1 ms: 1.43x faster                                               |
| nbody          | 93.0 ms                                                | 65.6 ms: 1.42x faster                                               |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.27x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 71.0 ms: 1.34x faster                                               |
| regex_dna      | 174 ms                                                 | 142 ms: 1.23x faster                                                |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                               |
| regex_effbot   | 2.46 ms                                                | 2.45 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.14x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 179 us: 1.56x faster                                                |
| unpickle_pure_python | 194 us                                                 | 133 us: 1.47x faster                                                |
| tomli_loads          | 1.71 sec                                               | 1.23 sec: 1.38x faster                                              |
| xml_etree_process    | 46.5 ms                                                | 34.2 ms: 1.36x faster                                               |
| json_dumps           | 8.11 ms                                                | 7.17 ms: 1.13x faster                                               |
| xml_etree_generate   | 53.5 ms                                                | 50.2 ms: 1.07x faster                                               |
| json_loads           | 16.4 us                                                | 16.6 us: 1.01x slower                                               |
| xml_etree_iterparse  | 72.1 ms                                                | 72.7 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.4 ms: 1.60x slower                                               |
| python_startup_no_site | 7.91 ms                                                | 13.5 ms: 1.70x slower                                               |
| Geometric mean         | (ref)                                                  | 1.65x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.45 ms: 1.53x faster                                               |
| django_template | 26.4 ms                                                | 20.4 ms: 1.29x faster                                               |
| genshi_text     | 17.3 ms                                                | 14.4 ms: 1.20x faster                                               |
| genshi_xml      | 33.8 ms                                                | 32.1 ms: 1.05x faster                                               |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 96.8 us: 3.34x faster                                               |
| deltablue                | 4.91 ms                                                | 2.32 ms: 2.12x faster                                               |
| deepcopy_memo            | 34.7 us                                                | 16.7 us: 2.08x faster                                               |
| async_tree_none          | 388 ms                                                 | 198 ms: 1.96x faster                                                |
| raytrace                 | 301 ms                                                 | 162 ms: 1.86x faster                                                |
| deepcopy                 | 272 us                                                 | 148 us: 1.83x faster                                                |
| async_tree_memoization   | 474 ms                                                 | 262 ms: 1.80x faster                                                |
| pylint                   | 277 ms                                                 | 162 ms: 1.71x faster                                                |
| asyncio_websockets       | 410 ms                                                 | 241 ms: 1.70x faster                                                |
| async_tree_io            | 980 ms                                                 | 580 ms: 1.69x faster                                                |
| logging_silent           | 117 ns                                                 | 69.4 ns: 1.69x faster                                               |
| go                       | 151 ms                                                 | 89.9 ms: 1.68x faster                                               |
| richards_super           | 57.8 ms                                                | 34.6 ms: 1.67x faster                                               |
| chaos                    | 65.8 ms                                                | 40.3 ms: 1.63x faster                                               |
| scimark_lu               | 103 ms                                                 | 65.0 ms: 1.58x faster                                               |
| pickle_pure_python       | 281 us                                                 | 179 us: 1.56x faster                                                |
| richards                 | 48.7 ms                                                | 31.1 ms: 1.56x faster                                               |
| mako                     | 9.87 ms                                                | 6.45 ms: 1.53x faster                                               |
| deepcopy_reduce          | 2.33 us                                                | 1.53 us: 1.52x faster                                               |
| sqlglot_parse            | 1.24 ms                                                | 822 us: 1.51x faster                                                |
| scimark_sor              | 128 ms                                                 | 86.1 ms: 1.49x faster                                               |
| unpickle_pure_python     | 194 us                                                 | 133 us: 1.47x faster                                                |
| logging_simple           | 4.45 us                                                | 3.04 us: 1.46x faster                                               |
| sqlglot_transpile        | 1.44 ms                                                | 993 us: 1.45x faster                                                |
| logging_format           | 4.83 us                                                | 3.33 us: 1.45x faster                                               |
| scimark_monte_carlo      | 65.6 ms                                                | 45.3 ms: 1.45x faster                                               |
| float                    | 69.0 ms                                                | 48.1 ms: 1.43x faster                                               |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 455 ms: 1.43x faster                                                |
| nbody                    | 93.0 ms                                                | 65.6 ms: 1.42x faster                                               |
| pprint_safe_repr         | 641 ms                                                 | 460 ms: 1.39x faster                                                |
| tomli_loads              | 1.71 sec                                               | 1.23 sec: 1.38x faster                                              |
| hexiom                   | 6.19 ms                                                | 4.49 ms: 1.38x faster                                               |
| pyflate                  | 427 ms                                                 | 312 ms: 1.37x faster                                                |
| spectral_norm            | 94.8 ms                                                | 69.3 ms: 1.37x faster                                               |
| thrift                   | 572 us                                                 | 419 us: 1.37x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 34.2 ms: 1.36x faster                                               |
| html5lib                 | 42.4 ms                                                | 31.1 ms: 1.36x faster                                               |
| generators               | 32.3 ms                                                | 24.1 ms: 1.34x faster                                               |
| regex_compile            | 95.3 ms                                                | 71.0 ms: 1.34x faster                                               |
| pprint_pformat           | 1.30 sec                                               | 974 ms: 1.34x faster                                                |
| pycparser                | 877 ms                                                 | 656 ms: 1.34x faster                                                |
| comprehensions           | 16.9 us                                                | 12.7 us: 1.33x faster                                               |
| crypto_pyaes             | 71.8 ms                                                | 54.3 ms: 1.32x faster                                               |
| django_template          | 26.4 ms                                                | 20.4 ms: 1.29x faster                                               |
| coroutines               | 20.7 ms                                                | 16.3 ms: 1.27x faster                                               |
| dulwich_log              | 35.3 ms                                                | 28.5 ms: 1.24x faster                                               |
| regex_dna                | 174 ms                                                 | 142 ms: 1.23x faster                                                |
| sympy_sum                | 92.2 ms                                                | 75.4 ms: 1.22x faster                                               |
| genshi_text              | 17.3 ms                                                | 14.4 ms: 1.20x faster                                               |
| fannkuch                 | 303 ms                                                 | 254 ms: 1.19x faster                                                |
| scimark_fft              | 224 ms                                                 | 190 ms: 1.18x faster                                                |
| tornado_http             | 86.7 ms                                                | 74.1 ms: 1.17x faster                                               |
| docutils                 | 1.73 sec                                               | 1.49 sec: 1.16x faster                                              |
| sympy_str                | 165 ms                                                 | 143 ms: 1.15x faster                                                |
| sympy_expand             | 269 ms                                                 | 237 ms: 1.13x faster                                                |
| json_dumps               | 8.11 ms                                                | 7.17 ms: 1.13x faster                                               |
| bench_thread_pool        | 527 us                                                 | 469 us: 1.12x faster                                                |
| 2to3                     | 192 ms                                                 | 171 ms: 1.12x faster                                                |
| sympy_integrate          | 13.1 ms                                                | 11.8 ms: 1.11x faster                                               |
| nqueens                  | 63.8 ms                                                | 57.9 ms: 1.10x faster                                               |
| sqlglot_normalize        | 190 ms                                                 | 173 ms: 1.10x faster                                                |
| pathlib                  | 24.5 ms                                                | 22.3 ms: 1.10x faster                                               |
| sqlglot_optimize         | 36.8 ms                                                | 33.6 ms: 1.09x faster                                               |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.15 ms: 1.09x faster                                               |
| json                     | 3.08 ms                                                | 2.84 ms: 1.08x faster                                               |
| mdp                      | 1.63 sec                                               | 1.52 sec: 1.07x faster                                              |
| meteor_contest           | 77.7 ms                                                | 72.9 ms: 1.07x faster                                               |
| xml_etree_generate       | 53.5 ms                                                | 50.2 ms: 1.07x faster                                               |
| genshi_xml               | 33.8 ms                                                | 32.1 ms: 1.05x faster                                               |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                               |
| regex_effbot             | 2.46 ms                                                | 2.45 ms: 1.00x faster                                               |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                |
| json_loads               | 16.4 us                                                | 16.6 us: 1.01x slower                                               |
| xml_etree_iterparse      | 72.1 ms                                                | 72.7 ms: 1.01x slower                                               |
| coverage                 | 41.5 ms                                                | 43.7 ms: 1.05x slower                                               |
| gc_traversal             | 2.36 ms                                                | 2.95 ms: 1.25x slower                                               |
| async_generators         | 231 ms                                                 | 291 ms: 1.26x slower                                                |
| telco                    | 3.49 ms                                                | 4.54 ms: 1.30x slower                                               |
| create_gc_cycles         | 860 us                                                 | 1.32 ms: 1.54x slower                                               |
| python_startup           | 10.9 ms                                                | 17.4 ms: 1.60x slower                                               |
| bench_mp_pool            | 37.4 ms                                                | 60.1 ms: 1.61x slower                                               |
| python_startup_no_site   | 7.91 ms                                                | 13.5 ms: 1.70x slower                                               |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                        |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.279x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.40x