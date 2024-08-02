# Results vs. 3.10.4

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: darwin-arm64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 159 ms: 1.21x faster                                                       |
| chameleon      | 6.26 ms                                                | 4.38 ms: 1.43x faster                                                      |
| docutils       | 1.73 sec                                               | 1.46 sec: 1.19x faster                                                     |
| html5lib       | 42.4 ms                                                | 31.2 ms: 1.36x faster                                                      |
| tornado_http   | 86.7 ms                                                | 72.4 ms: 1.20x faster                                                      |
| Geometric mean | (ref)                                                  | 1.27x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 255 ms: 1.86x faster                                                       |
| async_tree_none         | 388 ms                                                 | 210 ms: 1.85x faster                                                       |
| async_tree_io           | 980 ms                                                 | 561 ms: 1.74x faster                                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 465 ms: 1.40x faster                                                       |
| Geometric mean          | (ref)                                                  | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.3 ms: 1.57x faster                                                      |
| float          | 69.0 ms                                                | 48.6 ms: 1.42x faster                                                      |
| Geometric mean | (ref)                                                  | 1.31x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.7 ms: 1.39x faster                                                      |
| regex_dna      | 174 ms                                                 | 139 ms: 1.26x faster                                                       |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                      |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 181 us: 1.55x faster                                                       |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                                       |
| json_dumps           | 8.11 ms                                                | 6.14 ms: 1.32x faster                                                      |
| xml_etree_process    | 46.5 ms                                                | 37.0 ms: 1.26x faster                                                      |
| tomli_loads          | 1.71 sec                                               | 1.45 sec: 1.17x faster                                                     |
| xml_etree_parse      | 108 ms                                                 | 98.1 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 72.1 ms                                                | 67.7 ms: 1.07x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                | 53.1 ms: 1.01x faster                                                      |
| json_loads           | 16.4 us                                                | 17.2 us: 1.05x slower                                                      |
| pickle               | 6.97 us                                                | 7.44 us: 1.07x slower                                                      |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                      |
| pickle_list          | 2.74 us                                                | 2.99 us: 1.09x slower                                                      |
| unpickle             | 8.80 us                                                | 9.67 us: 1.10x slower                                                      |
| unpickle_list        | 2.69 us                                                | 3.26 us: 1.21x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 13.7 ms: 1.26x slower                                                      |
| python_startup_no_site | 7.91 ms                                                | 10.9 ms: 1.38x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.32x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.89 ms: 1.43x faster                                                      |
| django_template | 26.4 ms                                                | 19.4 ms: 1.36x faster                                                      |
| genshi_text     | 17.3 ms                                                | 13.9 ms: 1.25x faster                                                      |
| genshi_xml      | 33.8 ms                                                | 30.0 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 88.9 us: 3.63x faster                                                      |
| deltablue                | 4.91 ms                                                | 2.15 ms: 2.29x faster                                                      |
| raytrace                 | 301 ms                                                 | 148 ms: 2.03x faster                                                       |
| logging_silent           | 117 ns                                                 | 60.5 ns: 1.94x faster                                                      |
| chaos                    | 65.8 ms                                                | 34.7 ms: 1.90x faster                                                      |
| async_tree_memoization   | 474 ms                                                 | 255 ms: 1.86x faster                                                       |
| async_tree_none          | 388 ms                                                 | 210 ms: 1.85x faster                                                       |
| async_tree_io            | 980 ms                                                 | 561 ms: 1.74x faster                                                       |
| sqlglot_parse            | 1.24 ms                                                | 737 us: 1.69x faster                                                       |
| asyncio_tcp              | 659 ms                                                 | 398 ms: 1.66x faster                                                       |
| pylint                   | 277 ms                                                 | 168 ms: 1.64x faster                                                       |
| richards_super           | 57.8 ms                                                | 35.3 ms: 1.64x faster                                                      |
| sqlglot_transpile        | 1.44 ms                                                | 900 us: 1.60x faster                                                       |
| comprehensions           | 16.9 us                                                | 10.6 us: 1.59x faster                                                      |
| nbody                    | 93.0 ms                                                | 59.3 ms: 1.57x faster                                                      |
| crypto_pyaes             | 71.8 ms                                                | 45.8 ms: 1.57x faster                                                      |
| pickle_pure_python       | 281 us                                                 | 181 us: 1.55x faster                                                       |
| scimark_monte_carlo      | 65.6 ms                                                | 42.4 ms: 1.55x faster                                                      |
| scimark_lu               | 103 ms                                                 | 67.8 ms: 1.52x faster                                                      |
| deepcopy_memo            | 34.7 us                                                | 22.9 us: 1.51x faster                                                      |
| richards                 | 48.7 ms                                                | 32.2 ms: 1.51x faster                                                      |
| go                       | 151 ms                                                 | 99.7 ms: 1.51x faster                                                      |
| hexiom                   | 6.19 ms                                                | 4.10 ms: 1.51x faster                                                      |
| logging_simple           | 4.45 us                                                | 3.04 us: 1.46x faster                                                      |
| logging_format           | 4.83 us                                                | 3.33 us: 1.45x faster                                                      |
| mako                     | 9.87 ms                                                | 6.89 ms: 1.43x faster                                                      |
| generators               | 32.3 ms                                                | 22.6 ms: 1.43x faster                                                      |
| chameleon                | 6.26 ms                                                | 4.38 ms: 1.43x faster                                                      |
| spectral_norm            | 94.8 ms                                                | 66.5 ms: 1.42x faster                                                      |
| float                    | 69.0 ms                                                | 48.6 ms: 1.42x faster                                                      |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 465 ms: 1.40x faster                                                       |
| regex_compile            | 95.3 ms                                                | 68.7 ms: 1.39x faster                                                      |
| pycparser                | 877 ms                                                 | 634 ms: 1.38x faster                                                       |
| pprint_pformat           | 1.30 sec                                               | 949 ms: 1.37x faster                                                       |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                                       |
| pprint_safe_repr         | 641 ms                                                 | 469 ms: 1.37x faster                                                       |
| django_template          | 26.4 ms                                                | 19.4 ms: 1.36x faster                                                      |
| html5lib                 | 42.4 ms                                                | 31.2 ms: 1.36x faster                                                      |
| scimark_sor              | 128 ms                                                 | 95.1 ms: 1.35x faster                                                      |
| deepcopy                 | 272 us                                                 | 202 us: 1.34x faster                                                       |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                                       |
| sympy_sum                | 92.2 ms                                                | 69.4 ms: 1.33x faster                                                      |
| mypy2                    | 607 ms                                                 | 458 ms: 1.33x faster                                                       |
| json_dumps               | 8.11 ms                                                | 6.14 ms: 1.32x faster                                                      |
| deepcopy_reduce          | 2.33 us                                                | 1.78 us: 1.31x faster                                                      |
| thrift                   | 572 us                                                 | 440 us: 1.30x faster                                                       |
| dulwich_log              | 35.3 ms                                                | 27.3 ms: 1.29x faster                                                      |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.28x faster                                                      |
| coroutines               | 20.7 ms                                                | 16.4 ms: 1.26x faster                                                      |
| regex_dna                | 174 ms                                                 | 139 ms: 1.26x faster                                                       |
| xml_etree_process        | 46.5 ms                                                | 37.0 ms: 1.26x faster                                                      |
| sympy_str                | 165 ms                                                 | 132 ms: 1.25x faster                                                       |
| genshi_text              | 17.3 ms                                                | 13.9 ms: 1.25x faster                                                      |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.76 ms: 1.24x faster                                                      |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                                       |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.32 sec: 1.21x faster                                                     |
| nqueens                  | 63.8 ms                                                | 52.8 ms: 1.21x faster                                                      |
| 2to3                     | 192 ms                                                 | 159 ms: 1.21x faster                                                       |
| tornado_http             | 86.7 ms                                                | 72.4 ms: 1.20x faster                                                      |
| docutils                 | 1.73 sec                                               | 1.46 sec: 1.19x faster                                                     |
| sympy_expand             | 269 ms                                                 | 227 ms: 1.19x faster                                                       |
| sqlglot_optimize         | 36.8 ms                                                | 31.0 ms: 1.18x faster                                                      |
| tomli_loads              | 1.71 sec                                               | 1.45 sec: 1.17x faster                                                     |
| fannkuch                 | 303 ms                                                 | 258 ms: 1.17x faster                                                       |
| dask                     | 253 ms                                                 | 218 ms: 1.16x faster                                                       |
| gunicorn                 | 1.30 ms                                                | 1.13 ms: 1.15x faster                                                      |
| sqlglot_normalize        | 190 ms                                                 | 166 ms: 1.15x faster                                                       |
| bench_thread_pool        | 527 us                                                 | 461 us: 1.14x faster                                                       |
| aiohttp                  | 1.22 ms                                                | 1.08 ms: 1.13x faster                                                      |
| genshi_xml               | 33.8 ms                                                | 30.0 ms: 1.13x faster                                                      |
| xml_etree_parse          | 108 ms                                                 | 98.1 ms: 1.10x faster                                                      |
| mdp                      | 1.63 sec                                               | 1.50 sec: 1.09x faster                                                     |
| meteor_contest           | 77.7 ms                                                | 71.5 ms: 1.09x faster                                                      |
| pathlib                  | 24.5 ms                                                | 22.8 ms: 1.07x faster                                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 67.7 ms: 1.07x faster                                                      |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                      |
| json                     | 3.08 ms                                                | 3.03 ms: 1.02x faster                                                      |
| xml_etree_generate       | 53.5 ms                                                | 53.1 ms: 1.01x faster                                                      |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                      |
| json_loads               | 16.4 us                                                | 17.2 us: 1.05x slower                                                      |
| gc_traversal             | 2.36 ms                                                | 2.49 ms: 1.06x slower                                                      |
| sqlite_synth             | 1.46 us                                                | 1.55 us: 1.06x slower                                                      |
| pickle                   | 6.97 us                                                | 7.44 us: 1.07x slower                                                      |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                      |
| pickle_list              | 2.74 us                                                | 2.99 us: 1.09x slower                                                      |
| coverage                 | 41.5 ms                                                | 45.4 ms: 1.10x slower                                                      |
| create_gc_cycles         | 860 us                                                 | 946 us: 1.10x slower                                                       |
| unpickle                 | 8.80 us                                                | 9.67 us: 1.10x slower                                                      |
| async_generators         | 231 ms                                                 | 279 ms: 1.21x slower                                                       |
| unpickle_list            | 2.69 us                                                | 3.26 us: 1.21x slower                                                      |
| bench_mp_pool            | 37.4 ms                                                | 45.7 ms: 1.22x slower                                                      |
| telco                    | 3.49 ms                                                | 4.40 ms: 1.26x slower                                                      |
| python_startup           | 10.9 ms                                                | 13.7 ms: 1.26x slower                                                      |
| python_startup_no_site   | 7.91 ms                                                | 10.9 ms: 1.38x slower                                                      |
| flaskblogging            | 2.65 ms                                                | 5.18 ms: 1.96x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (12) of results/bm-20240504-3.13.0a6+-4c1049b/bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.17x