# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b1
- machine: darwin-arm64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.25x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 179 ms: 1.07x faster                                       |
| chameleon      | 6.26 ms                                                | 4.35 ms: 1.44x faster                                      |
| docutils       | 1.73 sec                                               | 1.46 sec: 1.19x faster                                     |
| html5lib       | 42.4 ms                                                | 31.2 ms: 1.36x faster                                      |
| tornado_http   | 86.7 ms                                                | 70.4 ms: 1.23x faster                                      |
| Geometric mean | (ref)                                                  | 1.25x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 210 ms: 1.85x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 258 ms: 1.83x faster                                       |
| async_tree_io           | 980 ms                                                 | 570 ms: 1.72x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 469 ms: 1.38x faster                                       |
| Geometric mean          | (ref)                                                  | 1.68x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 65.7 ms: 1.41x faster                                      |
| float          | 69.0 ms                                                | 49.0 ms: 1.41x faster                                      |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.26x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.2 ms: 1.40x faster                                      |
| regex_dna      | 174 ms                                                 | 139 ms: 1.26x faster                                       |
| regex_v8       | 17.1 ms                                                | 16.8 ms: 1.02x faster                                      |
| regex_effbot   | 2.46 ms                                                | 2.55 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 181 us: 1.55x faster                                       |
| unpickle_pure_python | 194 us                                                 | 141 us: 1.38x faster                                       |
| json_dumps           | 8.11 ms                                                | 6.35 ms: 1.28x faster                                      |
| xml_etree_process    | 46.5 ms                                                | 37.1 ms: 1.25x faster                                      |
| tomli_loads          | 1.71 sec                                               | 1.45 sec: 1.17x faster                                     |
| xml_etree_parse      | 108 ms                                                 | 97.6 ms: 1.10x faster                                      |
| xml_etree_iterparse  | 72.1 ms                                                | 67.5 ms: 1.07x faster                                      |
| xml_etree_generate   | 53.5 ms                                                | 51.8 ms: 1.03x faster                                      |
| json_loads           | 16.4 us                                                | 17.3 us: 1.05x slower                                      |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| pickle               | 6.97 us                                                | 7.47 us: 1.07x slower                                      |
| pickle_list          | 2.74 us                                                | 2.98 us: 1.09x slower                                      |
| unpickle             | 8.80 us                                                | 9.70 us: 1.10x slower                                      |
| unpickle_list        | 2.69 us                                                | 3.31 us: 1.23x slower                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.3 ms: 1.32x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 11.6 ms: 1.46x slower                                      |
| Geometric mean         | (ref)                                                  | 1.39x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.88 ms: 1.44x faster                                      |
| django_template | 26.4 ms                                                | 19.4 ms: 1.36x faster                                      |
| genshi_text     | 17.3 ms                                                | 13.8 ms: 1.25x faster                                      |
| genshi_xml      | 33.8 ms                                                | 30.0 ms: 1.13x faster                                      |
| Geometric mean  | (ref)                                                  | 1.29x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.5 us: 3.49x faster                                      |
| deltablue                | 4.91 ms                                                | 2.15 ms: 2.29x faster                                      |
| raytrace                 | 301 ms                                                 | 150 ms: 2.01x faster                                       |
| logging_silent           | 117 ns                                                 | 60.1 ns: 1.95x faster                                      |
| async_tree_none          | 388 ms                                                 | 210 ms: 1.85x faster                                       |
| chaos                    | 65.8 ms                                                | 35.9 ms: 1.83x faster                                      |
| async_tree_memoization   | 474 ms                                                 | 258 ms: 1.83x faster                                       |
| async_tree_io            | 980 ms                                                 | 570 ms: 1.72x faster                                       |
| sqlglot_parse            | 1.24 ms                                                | 739 us: 1.68x faster                                       |
| richards_super           | 57.8 ms                                                | 35.2 ms: 1.64x faster                                      |
| pylint                   | 277 ms                                                 | 169 ms: 1.64x faster                                       |
| sqlglot_transpile        | 1.44 ms                                                | 897 us: 1.61x faster                                       |
| comprehensions           | 16.9 us                                                | 10.9 us: 1.56x faster                                      |
| asyncio_tcp              | 659 ms                                                 | 424 ms: 1.55x faster                                       |
| deepcopy_memo            | 34.7 us                                                | 22.4 us: 1.55x faster                                      |
| pickle_pure_python       | 281 us                                                 | 181 us: 1.55x faster                                       |
| richards                 | 48.7 ms                                                | 31.9 ms: 1.53x faster                                      |
| scimark_monte_carlo      | 65.6 ms                                                | 43.0 ms: 1.52x faster                                      |
| hexiom                   | 6.19 ms                                                | 4.09 ms: 1.52x faster                                      |
| scimark_lu               | 103 ms                                                 | 68.3 ms: 1.51x faster                                      |
| go                       | 151 ms                                                 | 100 ms: 1.51x faster                                       |
| logging_simple           | 4.45 us                                                | 3.06 us: 1.45x faster                                      |
| chameleon                | 6.26 ms                                                | 4.35 ms: 1.44x faster                                      |
| logging_format           | 4.83 us                                                | 3.36 us: 1.44x faster                                      |
| mako                     | 9.87 ms                                                | 6.88 ms: 1.44x faster                                      |
| crypto_pyaes             | 71.8 ms                                                | 50.3 ms: 1.43x faster                                      |
| generators               | 32.3 ms                                                | 22.7 ms: 1.43x faster                                      |
| nbody                    | 93.0 ms                                                | 65.7 ms: 1.41x faster                                      |
| float                    | 69.0 ms                                                | 49.0 ms: 1.41x faster                                      |
| regex_compile            | 95.3 ms                                                | 68.2 ms: 1.40x faster                                      |
| spectral_norm            | 94.8 ms                                                | 68.2 ms: 1.39x faster                                      |
| pycparser                | 877 ms                                                 | 630 ms: 1.39x faster                                       |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 469 ms: 1.38x faster                                       |
| pprint_pformat           | 1.30 sec                                               | 947 ms: 1.38x faster                                       |
| unpickle_pure_python     | 194 us                                                 | 141 us: 1.38x faster                                       |
| pprint_safe_repr         | 641 ms                                                 | 468 ms: 1.37x faster                                       |
| django_template          | 26.4 ms                                                | 19.4 ms: 1.36x faster                                      |
| html5lib                 | 42.4 ms                                                | 31.2 ms: 1.36x faster                                      |
| deepcopy                 | 272 us                                                 | 203 us: 1.34x faster                                       |
| pyflate                  | 427 ms                                                 | 319 ms: 1.34x faster                                       |
| scimark_sor              | 128 ms                                                 | 96.3 ms: 1.33x faster                                      |
| thrift                   | 572 us                                                 | 434 us: 1.32x faster                                       |
| mypy2                    | 607 ms                                                 | 461 ms: 1.32x faster                                       |
| sympy_sum                | 92.2 ms                                                | 70.2 ms: 1.31x faster                                      |
| deepcopy_reduce          | 2.33 us                                                | 1.79 us: 1.30x faster                                      |
| dulwich_log              | 35.3 ms                                                | 27.3 ms: 1.29x faster                                      |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.28x faster                                      |
| json_dumps               | 8.11 ms                                                | 6.35 ms: 1.28x faster                                      |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.27x faster                                      |
| regex_dna                | 174 ms                                                 | 139 ms: 1.26x faster                                       |
| xml_etree_process        | 46.5 ms                                                | 37.1 ms: 1.25x faster                                      |
| genshi_text              | 17.3 ms                                                | 13.8 ms: 1.25x faster                                      |
| sympy_str                | 165 ms                                                 | 133 ms: 1.25x faster                                       |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                     |
| tornado_http             | 86.7 ms                                                | 70.4 ms: 1.23x faster                                      |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.80 ms: 1.22x faster                                      |
| nqueens                  | 63.8 ms                                                | 52.8 ms: 1.21x faster                                      |
| fannkuch                 | 303 ms                                                 | 252 ms: 1.20x faster                                       |
| docutils                 | 1.73 sec                                               | 1.46 sec: 1.19x faster                                     |
| sqlglot_optimize         | 36.8 ms                                                | 31.1 ms: 1.18x faster                                      |
| scimark_fft              | 224 ms                                                 | 190 ms: 1.18x faster                                       |
| sympy_expand             | 269 ms                                                 | 228 ms: 1.18x faster                                       |
| tomli_loads              | 1.71 sec                                               | 1.45 sec: 1.17x faster                                     |
| gunicorn                 | 1.30 ms                                                | 1.11 ms: 1.17x faster                                      |
| dask                     | 253 ms                                                 | 219 ms: 1.16x faster                                       |
| sqlglot_normalize        | 190 ms                                                 | 166 ms: 1.14x faster                                       |
| bench_thread_pool        | 527 us                                                 | 464 us: 1.14x faster                                       |
| genshi_xml               | 33.8 ms                                                | 30.0 ms: 1.13x faster                                      |
| aiohttp                  | 1.22 ms                                                | 1.10 ms: 1.12x faster                                      |
| xml_etree_parse          | 108 ms                                                 | 97.6 ms: 1.10x faster                                      |
| meteor_contest           | 77.7 ms                                                | 70.6 ms: 1.10x faster                                      |
| mdp                      | 1.63 sec                                               | 1.50 sec: 1.09x faster                                     |
| pathlib                  | 24.5 ms                                                | 22.7 ms: 1.08x faster                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 67.5 ms: 1.07x faster                                      |
| 2to3                     | 192 ms                                                 | 179 ms: 1.07x faster                                       |
| xml_etree_generate       | 53.5 ms                                                | 51.8 ms: 1.03x faster                                      |
| json                     | 3.08 ms                                                | 2.99 ms: 1.03x faster                                      |
| regex_v8                 | 17.1 ms                                                | 16.8 ms: 1.02x faster                                      |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                       |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                       |
| create_gc_cycles         | 860 us                                                 | 884 us: 1.03x slower                                       |
| regex_effbot             | 2.46 ms                                                | 2.55 ms: 1.04x slower                                      |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                      |
| json_loads               | 16.4 us                                                | 17.3 us: 1.05x slower                                      |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.05x slower                                      |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| pickle                   | 6.97 us                                                | 7.47 us: 1.07x slower                                      |
| pickle_list              | 2.74 us                                                | 2.98 us: 1.09x slower                                      |
| unpickle                 | 8.80 us                                                | 9.70 us: 1.10x slower                                      |
| coverage                 | 41.5 ms                                                | 46.5 ms: 1.12x slower                                      |
| async_generators         | 231 ms                                                 | 278 ms: 1.20x slower                                       |
| bench_mp_pool            | 37.4 ms                                                | 45.2 ms: 1.21x slower                                      |
| unpickle_list            | 2.69 us                                                | 3.31 us: 1.23x slower                                      |
| telco                    | 3.49 ms                                                | 4.56 ms: 1.31x slower                                      |
| python_startup           | 10.9 ms                                                | 14.3 ms: 1.32x slower                                      |
| python_startup_no_site   | 7.91 ms                                                | 11.6 ms: 1.46x slower                                      |
| flaskblogging            | 2.65 ms                                                | 5.10 ms: 1.93x slower                                      |
| Geometric mean           | (ref)                                                  | 1.25x faster                                               |
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (12) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.17x