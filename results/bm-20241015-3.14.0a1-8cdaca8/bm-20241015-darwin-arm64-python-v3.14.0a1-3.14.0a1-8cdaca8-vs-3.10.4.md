# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a1
- machine: darwin-arm64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.285x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.20x faster                                       |
| docutils       | 1.73 sec                                               | 1.41 sec: 1.23x faster                                     |
| html5lib       | 42.4 ms                                                | 31.8 ms: 1.33x faster                                      |
| Geometric mean | (ref)                                                  | 1.23x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 196 ms: 1.98x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 243 ms: 1.95x faster                                       |
| async_tree_io           | 980 ms                                                 | 580 ms: 1.69x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 455 ms: 1.43x faster                                       |
| Geometric mean          | (ref)                                                  | 1.75x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 65.5 ms: 1.42x faster                                      |
| float          | 69.0 ms                                                | 49.7 ms: 1.39x faster                                      |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.25x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.4 ms: 1.39x faster                                      |
| regex_dna      | 174 ms                                                 | 146 ms: 1.20x faster                                       |
| regex_v8       | 17.1 ms                                                | 16.5 ms: 1.04x faster                                      |
| regex_effbot   | 2.46 ms                                                | 2.59 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 186 us: 1.51x faster                                       |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                       |
| xml_etree_process    | 46.5 ms                                                | 37.5 ms: 1.24x faster                                      |
| tomli_loads          | 1.71 sec                                               | 1.50 sec: 1.14x faster                                     |
| json_dumps           | 8.11 ms                                                | 7.18 ms: 1.13x faster                                      |
| xml_etree_generate   | 53.5 ms                                                | 52.5 ms: 1.02x faster                                      |
| unpickle             | 8.80 us                                                | 9.03 us: 1.03x slower                                      |
| xml_etree_iterparse  | 72.1 ms                                                | 75.1 ms: 1.04x slower                                      |
| pickle               | 6.97 us                                                | 7.33 us: 1.05x slower                                      |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.06x slower                                      |
| pickle_list          | 2.74 us                                                | 2.98 us: 1.09x slower                                      |
| unpickle_list        | 2.69 us                                                | 3.01 us: 1.12x slower                                      |
| Geometric mean       | (ref)                                                  | 1.06x faster                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 19.0 ms: 1.75x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 14.7 ms: 1.86x slower                                      |
| Geometric mean         | (ref)                                                  | 1.81x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.01 ms: 1.41x faster                                      |
| django_template | 26.4 ms                                                | 19.8 ms: 1.34x faster                                      |
| genshi_text     | 17.3 ms                                                | 13.7 ms: 1.27x faster                                      |
| genshi_xml      | 33.8 ms                                                | 29.8 ms: 1.13x faster                                      |
| Geometric mean  | (ref)                                                  | 1.28x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.3 us: 3.50x faster                                      |
| deltablue                | 4.91 ms                                                | 2.23 ms: 2.21x faster                                      |
| deepcopy_memo            | 34.7 us                                                | 17.4 us: 1.99x faster                                      |
| async_tree_none          | 388 ms                                                 | 196 ms: 1.98x faster                                       |
| raytrace                 | 301 ms                                                 | 154 ms: 1.96x faster                                       |
| async_tree_memoization   | 474 ms                                                 | 243 ms: 1.95x faster                                       |
| logging_silent           | 117 ns                                                 | 60.9 ns: 1.92x faster                                      |
| deepcopy                 | 272 us                                                 | 146 us: 1.87x faster                                       |
| go                       | 151 ms                                                 | 82.1 ms: 1.83x faster                                      |
| chaos                    | 65.8 ms                                                | 37.3 ms: 1.76x faster                                      |
| asyncio_websockets       | 410 ms                                                 | 241 ms: 1.70x faster                                       |
| async_tree_io            | 980 ms                                                 | 580 ms: 1.69x faster                                       |
| richards_super           | 57.8 ms                                                | 34.3 ms: 1.68x faster                                      |
| sqlglot_parse            | 1.24 ms                                                | 743 us: 1.67x faster                                       |
| generators               | 32.3 ms                                                | 20.1 ms: 1.61x faster                                      |
| sqlglot_transpile        | 1.44 ms                                                | 901 us: 1.60x faster                                       |
| richards                 | 48.7 ms                                                | 31.0 ms: 1.57x faster                                      |
| pylint                   | 277 ms                                                 | 180 ms: 1.54x faster                                       |
| deepcopy_reduce          | 2.33 us                                                | 1.52 us: 1.53x faster                                      |
| comprehensions           | 16.9 us                                                | 11.1 us: 1.52x faster                                      |
| pickle_pure_python       | 281 us                                                 | 186 us: 1.51x faster                                       |
| asyncio_tcp              | 659 ms                                                 | 437 ms: 1.51x faster                                       |
| scimark_lu               | 103 ms                                                 | 68.2 ms: 1.51x faster                                      |
| scimark_monte_carlo      | 65.6 ms                                                | 43.6 ms: 1.50x faster                                      |
| hexiom                   | 6.19 ms                                                | 4.13 ms: 1.50x faster                                      |
| unpack_sequence          | 39.0 ns                                                | 26.8 ns: 1.46x faster                                      |
| logging_simple           | 4.45 us                                                | 3.08 us: 1.44x faster                                      |
| logging_format           | 4.83 us                                                | 3.35 us: 1.44x faster                                      |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 455 ms: 1.43x faster                                       |
| nbody                    | 93.0 ms                                                | 65.5 ms: 1.42x faster                                      |
| mako                     | 9.87 ms                                                | 7.01 ms: 1.41x faster                                      |
| regex_compile            | 95.3 ms                                                | 68.4 ms: 1.39x faster                                      |
| pprint_pformat           | 1.30 sec                                               | 936 ms: 1.39x faster                                       |
| crypto_pyaes             | 71.8 ms                                                | 51.7 ms: 1.39x faster                                      |
| float                    | 69.0 ms                                                | 49.7 ms: 1.39x faster                                      |
| pprint_safe_repr         | 641 ms                                                 | 462 ms: 1.39x faster                                       |
| pycparser                | 877 ms                                                 | 635 ms: 1.38x faster                                       |
| thrift                   | 572 us                                                 | 416 us: 1.38x faster                                       |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                       |
| spectral_norm            | 94.8 ms                                                | 70.2 ms: 1.35x faster                                      |
| scimark_sor              | 128 ms                                                 | 95.9 ms: 1.34x faster                                      |
| django_template          | 26.4 ms                                                | 19.8 ms: 1.34x faster                                      |
| html5lib                 | 42.4 ms                                                | 31.8 ms: 1.33x faster                                      |
| sympy_sum                | 92.2 ms                                                | 69.6 ms: 1.32x faster                                      |
| pyflate                  | 427 ms                                                 | 327 ms: 1.31x faster                                       |
| dulwich_log              | 35.3 ms                                                | 27.3 ms: 1.29x faster                                      |
| genshi_text              | 17.3 ms                                                | 13.7 ms: 1.27x faster                                      |
| coroutines               | 20.7 ms                                                | 16.5 ms: 1.25x faster                                      |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                     |
| xml_etree_process        | 46.5 ms                                                | 37.5 ms: 1.24x faster                                      |
| sympy_str                | 165 ms                                                 | 133 ms: 1.24x faster                                       |
| docutils                 | 1.73 sec                                               | 1.41 sec: 1.23x faster                                     |
| bench_thread_pool        | 527 us                                                 | 433 us: 1.22x faster                                       |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.83 ms: 1.21x faster                                      |
| 2to3                     | 192 ms                                                 | 160 ms: 1.20x faster                                       |
| sympy_integrate          | 13.1 ms                                                | 11.0 ms: 1.20x faster                                      |
| regex_dna                | 174 ms                                                 | 146 ms: 1.20x faster                                       |
| nqueens                  | 63.8 ms                                                | 53.6 ms: 1.19x faster                                      |
| sympy_expand             | 269 ms                                                 | 227 ms: 1.19x faster                                       |
| sqlglot_optimize         | 36.8 ms                                                | 31.1 ms: 1.18x faster                                      |
| scimark_fft              | 224 ms                                                 | 190 ms: 1.18x faster                                       |
| sqlglot_normalize        | 190 ms                                                 | 166 ms: 1.14x faster                                       |
| tomli_loads              | 1.71 sec                                               | 1.50 sec: 1.14x faster                                     |
| genshi_xml               | 33.8 ms                                                | 29.8 ms: 1.13x faster                                      |
| fannkuch                 | 303 ms                                                 | 268 ms: 1.13x faster                                       |
| json_dumps               | 8.11 ms                                                | 7.18 ms: 1.13x faster                                      |
| mdp                      | 1.63 sec                                               | 1.46 sec: 1.11x faster                                     |
| pathlib                  | 24.5 ms                                                | 22.0 ms: 1.11x faster                                      |
| meteor_contest           | 77.7 ms                                                | 70.5 ms: 1.10x faster                                      |
| json                     | 3.08 ms                                                | 2.87 ms: 1.07x faster                                      |
| regex_v8                 | 17.1 ms                                                | 16.5 ms: 1.04x faster                                      |
| xml_etree_generate       | 53.5 ms                                                | 52.5 ms: 1.02x faster                                      |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                       |
| unpickle                 | 8.80 us                                                | 9.03 us: 1.03x slower                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 75.1 ms: 1.04x slower                                      |
| sqlite_synth             | 1.46 us                                                | 1.52 us: 1.04x slower                                      |
| pickle                   | 6.97 us                                                | 7.33 us: 1.05x slower                                      |
| regex_effbot             | 2.46 ms                                                | 2.59 ms: 1.05x slower                                      |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.06x slower                                      |
| coverage                 | 41.5 ms                                                | 44.8 ms: 1.08x slower                                      |
| pickle_list              | 2.74 us                                                | 2.98 us: 1.09x slower                                      |
| unpickle_list            | 2.69 us                                                | 3.01 us: 1.12x slower                                      |
| async_generators         | 231 ms                                                 | 276 ms: 1.19x slower                                       |
| gc_traversal             | 2.36 ms                                                | 2.94 ms: 1.24x slower                                      |
| telco                    | 3.49 ms                                                | 4.53 ms: 1.30x slower                                      |
| create_gc_cycles         | 860 us                                                 | 1.30 ms: 1.51x slower                                      |
| bench_mp_pool            | 37.4 ms                                                | 58.9 ms: 1.58x slower                                      |
| python_startup           | 10.9 ms                                                | 19.0 ms: 1.75x slower                                      |
| python_startup_no_site   | 7.91 ms                                                | 14.7 ms: 1.86x slower                                      |
| Geometric mean           | (ref)                                                  | 1.26x faster                                               |

Benchmark hidden because not significant (3): tornado_http, json_loads, xml_etree_parse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.285x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.32x