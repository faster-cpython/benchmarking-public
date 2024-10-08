# Results vs. 3.10.4

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.12x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 246 ms: 1.29x slower                                                  |
| docutils       | 1.73 sec                                               | 1.75 sec: 1.01x slower                                                |
| html5lib       | 42.4 ms                                                | 51.2 ms: 1.21x slower                                                 |
| tornado_http   | 86.7 ms                                                | 127 ms: 1.46x slower                                                  |
| Geometric mean | (ref)                                                  | 1.23x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 525 ms: 1.87x faster                                                  |
| async_tree_none         | 388 ms                                                 | 233 ms: 1.66x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 288 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 485 ms: 1.34x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.62x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 69.0 ms                                                | 93.8 ms: 1.36x slower                                                 |
| nbody          | 93.0 ms                                                | 154 ms: 1.66x slower                                                  |
| Geometric mean | (ref)                                                  | 1.31x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 139 ms: 1.26x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.44 ms: 1.01x faster                                                 |
| regex_v8       | 17.1 ms                                                | 17.1 ms: 1.00x faster                                                 |
| regex_compile  | 95.3 ms                                                | 119 ms: 1.25x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.11 ms                                                | 7.74 ms: 1.05x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| pickle               | 6.97 us                                                | 7.05 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 75.6 ms: 1.05x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.90 us: 1.06x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.4 us: 1.08x slower                                                 |
| unpickle             | 8.80 us                                                | 9.72 us: 1.11x slower                                                 |
| json_loads           | 16.4 us                                                | 18.8 us: 1.14x slower                                                 |
| tomli_loads          | 1.71 sec                                               | 1.99 sec: 1.17x slower                                                |
| unpickle_list        | 2.69 us                                                | 3.25 us: 1.21x slower                                                 |
| xml_etree_process    | 46.5 ms                                                | 57.2 ms: 1.23x slower                                                 |
| pickle_pure_python   | 281 us                                                 | 346 us: 1.23x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 68.1 ms: 1.27x slower                                                 |
| unpickle_pure_python | 194 us                                                 | 262 us: 1.35x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.0 ms: 1.56x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.6 ms: 1.72x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.64x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 26.4 ms                                                | 35.3 ms: 1.34x slower                                                 |
| mako            | 9.87 ms                                                | 13.3 ms: 1.35x slower                                                 |
| genshi_text     | 17.3 ms                                                | 24.9 ms: 1.44x slower                                                 |
| genshi_xml      | 33.8 ms                                                | 49.6 ms: 1.47x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.40x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 142 us: 2.28x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 335 ms: 1.97x faster                                                  |
| async_tree_io            | 980 ms                                                 | 525 ms: 1.87x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 102 ms: 1.86x faster                                                  |
| async_tree_none          | 388 ms                                                 | 233 ms: 1.66x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 288 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 485 ms: 1.34x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.24 sec: 1.29x faster                                                |
| pylint                   | 277 ms                                                 | 215 ms: 1.29x faster                                                  |
| regex_dna                | 174 ms                                                 | 139 ms: 1.26x faster                                                  |
| create_gc_cycles         | 860 us                                                 | 686 us: 1.25x faster                                                  |
| gc_traversal             | 2.36 ms                                                | 2.05 ms: 1.15x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 31.2 us: 1.11x faster                                                 |
| deepcopy                 | 272 us                                                 | 245 us: 1.11x faster                                                  |
| json_dumps               | 8.11 ms                                                | 7.74 ms: 1.05x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 405 ms: 1.01x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.44 ms: 1.01x faster                                                 |
| pidigits                 | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.1 ms: 1.00x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.75 sec: 1.01x slower                                                |
| pickle                   | 6.97 us                                                | 7.05 us: 1.01x slower                                                 |
| pycparser                | 877 ms                                                 | 913 ms: 1.04x slower                                                  |
| pathlib                  | 24.5 ms                                                | 25.6 ms: 1.05x slower                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 75.6 ms: 1.05x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.53 us: 1.05x slower                                                 |
| deepcopy_reduce          | 2.33 us                                                | 2.46 us: 1.06x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.90 us: 1.06x slower                                                 |
| generators               | 32.3 ms                                                | 34.6 ms: 1.07x slower                                                 |
| crypto_pyaes             | 71.8 ms                                                | 77.4 ms: 1.08x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.4 us: 1.08x slower                                                 |
| json                     | 3.08 ms                                                | 3.35 ms: 1.09x slower                                                 |
| comprehensions           | 16.9 us                                                | 18.7 us: 1.10x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.72 us: 1.11x slower                                                 |
| richards_super           | 57.8 ms                                                | 64.3 ms: 1.11x slower                                                 |
| pyflate                  | 427 ms                                                 | 479 ms: 1.12x slower                                                  |
| mdp                      | 1.63 sec                                               | 1.83 sec: 1.12x slower                                                |
| chaos                    | 65.8 ms                                                | 74.2 ms: 1.13x slower                                                 |
| meteor_contest           | 77.7 ms                                                | 88.7 ms: 1.14x slower                                                 |
| richards                 | 48.7 ms                                                | 55.6 ms: 1.14x slower                                                 |
| json_loads               | 16.4 us                                                | 18.8 us: 1.14x slower                                                 |
| deltablue                | 4.91 ms                                                | 5.63 ms: 1.15x slower                                                 |
| dulwich_log              | 35.3 ms                                                | 40.7 ms: 1.15x slower                                                 |
| logging_silent           | 117 ns                                                 | 135 ns: 1.15x slower                                                  |
| fannkuch                 | 303 ms                                                 | 352 ms: 1.16x slower                                                  |
| tomli_loads              | 1.71 sec                                               | 1.99 sec: 1.17x slower                                                |
| scimark_fft              | 224 ms                                                 | 263 ms: 1.17x slower                                                  |
| sympy_integrate          | 13.1 ms                                                | 15.4 ms: 1.17x slower                                                 |
| nqueens                  | 63.8 ms                                                | 75.5 ms: 1.18x slower                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 4.06 ms: 1.19x slower                                                 |
| thrift                   | 572 us                                                 | 679 us: 1.19x slower                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 78.1 ms: 1.19x slower                                                 |
| go                       | 151 ms                                                 | 181 ms: 1.20x slower                                                  |
| unpickle_list            | 2.69 us                                                | 3.25 us: 1.21x slower                                                 |
| coroutines               | 20.7 ms                                                | 25.0 ms: 1.21x slower                                                 |
| html5lib                 | 42.4 ms                                                | 51.2 ms: 1.21x slower                                                 |
| xml_etree_process        | 46.5 ms                                                | 57.2 ms: 1.23x slower                                                 |
| hexiom                   | 6.19 ms                                                | 7.63 ms: 1.23x slower                                                 |
| pickle_pure_python       | 281 us                                                 | 346 us: 1.23x slower                                                  |
| raytrace                 | 301 ms                                                 | 373 ms: 1.24x slower                                                  |
| spectral_norm            | 94.8 ms                                                | 118 ms: 1.24x slower                                                  |
| regex_compile            | 95.3 ms                                                | 119 ms: 1.25x slower                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.64 sec: 1.26x slower                                                |
| pprint_safe_repr         | 641 ms                                                 | 808 ms: 1.26x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 68.1 ms: 1.27x slower                                                 |
| 2to3                     | 192 ms                                                 | 246 ms: 1.29x slower                                                  |
| scimark_sor              | 128 ms                                                 | 165 ms: 1.29x slower                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.88 ms: 1.30x slower                                                 |
| sqlglot_parse            | 1.24 ms                                                | 1.64 ms: 1.32x slower                                                 |
| django_template          | 26.4 ms                                                | 35.3 ms: 1.34x slower                                                 |
| coverage                 | 41.5 ms                                                | 55.6 ms: 1.34x slower                                                 |
| mako                     | 9.87 ms                                                | 13.3 ms: 1.35x slower                                                 |
| unpickle_pure_python     | 194 us                                                 | 262 us: 1.35x slower                                                  |
| float                    | 69.0 ms                                                | 93.8 ms: 1.36x slower                                                 |
| logging_simple           | 4.45 us                                                | 6.05 us: 1.36x slower                                                 |
| logging_format           | 4.83 us                                                | 6.60 us: 1.37x slower                                                 |
| sympy_str                | 165 ms                                                 | 227 ms: 1.37x slower                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 50.9 ms: 1.38x slower                                                 |
| scimark_lu               | 103 ms                                                 | 144 ms: 1.40x slower                                                  |
| async_generators         | 231 ms                                                 | 331 ms: 1.43x slower                                                  |
| genshi_text              | 17.3 ms                                                | 24.9 ms: 1.44x slower                                                 |
| tornado_http             | 86.7 ms                                                | 127 ms: 1.46x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 49.6 ms: 1.47x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 54.9 ms: 1.47x slower                                                 |
| sympy_sum                | 92.2 ms                                                | 137 ms: 1.49x slower                                                  |
| bench_thread_pool        | 527 us                                                 | 792 us: 1.50x slower                                                  |
| python_startup           | 10.9 ms                                                | 17.0 ms: 1.56x slower                                                 |
| sympy_expand             | 269 ms                                                 | 421 ms: 1.56x slower                                                  |
| telco                    | 3.49 ms                                                | 5.69 ms: 1.63x slower                                                 |
| nbody                    | 93.0 ms                                                | 154 ms: 1.66x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 13.6 ms: 1.72x slower                                                 |
| unpack_sequence          | 39.0 ns                                                | 96.0 ns: 2.46x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.12x slower                                                          |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240920-3.14.0a0-342e654-NOGIL/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 0.86x