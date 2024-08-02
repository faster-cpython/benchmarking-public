# Results vs. 3.10.4

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: darwin-arm64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 0.78x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 159 ms: 1.20x faster                                                   |
| chameleon      | 6.26 ms                                                | 4.29 ms: 1.46x faster                                                  |
| docutils       | 1.73 sec                                               | 1.43 sec: 1.21x faster                                                 |
| html5lib       | 42.4 ms                                                | 31.1 ms: 1.36x faster                                                  |
| tornado_http   | 86.7 ms                                                | 65.5 ms: 1.33x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 206 ms: 1.89x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 255 ms: 1.86x faster                                                   |
| async_tree_io           | 980 ms                                                 | 551 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 462 ms: 1.40x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.72x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.8 ms: 1.56x faster                                                  |
| float          | 69.0 ms                                                | 48.1 ms: 1.43x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.0 ms: 1.40x faster                                                  |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                   |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                  |
| regex_effbot   | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 179 us: 1.57x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 141 us: 1.38x faster                                                   |
| json_dumps           | 8.11 ms                                                | 6.18 ms: 1.31x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 36.9 ms: 1.26x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.46 sec: 1.17x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.02x faster                                                   |
| xml_etree_generate   | 53.5 ms                                                | 52.5 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 71.6 ms: 1.01x faster                                                  |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| unpickle             | 8.80 us                                                | 9.14 us: 1.04x slower                                                  |
| unpickle_list        | 2.69 us                                                | 2.88 us: 1.07x slower                                                  |
| pickle               | 6.97 us                                                | 7.51 us: 1.08x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.6 us: 1.10x slower                                                  |
| pickle_list          | 2.74 us                                                | 3.02 us: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 13.3 ms: 1.22x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 10.3 ms: 1.30x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.97 ms: 1.42x faster                                                  |
| django_template | 26.4 ms                                                | 19.3 ms: 1.37x faster                                                  |
| genshi_text     | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 30.2 ms: 1.12x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 88.2 us: 3.66x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.14 ms: 2.30x faster                                                  |
| raytrace                 | 301 ms                                                 | 147 ms: 2.05x faster                                                   |
| logging_silent           | 117 ns                                                 | 60.3 ns: 1.94x faster                                                  |
| chaos                    | 65.8 ms                                                | 34.1 ms: 1.93x faster                                                  |
| async_tree_none          | 388 ms                                                 | 206 ms: 1.89x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 255 ms: 1.86x faster                                                   |
| async_tree_io            | 980 ms                                                 | 551 ms: 1.78x faster                                                   |
| sqlglot_parse            | 1.24 ms                                                | 731 us: 1.70x faster                                                   |
| asyncio_tcp              | 659 ms                                                 | 389 ms: 1.70x faster                                                   |
| comprehensions           | 16.9 us                                                | 10.2 us: 1.66x faster                                                  |
| pylint                   | 277 ms                                                 | 168 ms: 1.65x faster                                                   |
| richards_super           | 57.8 ms                                                | 35.2 ms: 1.64x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 891 us: 1.62x faster                                                   |
| mypy2                    | 607 ms                                                 | 376 ms: 1.62x faster                                                   |
| pickle_pure_python       | 281 us                                                 | 179 us: 1.57x faster                                                   |
| scimark_lu               | 103 ms                                                 | 66.0 ms: 1.56x faster                                                  |
| nbody                    | 93.0 ms                                                | 59.8 ms: 1.56x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 42.4 ms: 1.55x faster                                                  |
| richards                 | 48.7 ms                                                | 31.7 ms: 1.53x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 22.6 us: 1.53x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.07 ms: 1.52x faster                                                  |
| go                       | 151 ms                                                 | 100 ms: 1.50x faster                                                   |
| logging_simple           | 4.45 us                                                | 3.04 us: 1.47x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 49.2 ms: 1.46x faster                                                  |
| chameleon                | 6.26 ms                                                | 4.29 ms: 1.46x faster                                                  |
| logging_format           | 4.83 us                                                | 3.32 us: 1.45x faster                                                  |
| float                    | 69.0 ms                                                | 48.1 ms: 1.43x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 66.3 ms: 1.43x faster                                                  |
| generators               | 32.3 ms                                                | 22.7 ms: 1.42x faster                                                  |
| mako                     | 9.87 ms                                                | 6.97 ms: 1.42x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 462 ms: 1.40x faster                                                   |
| regex_compile            | 95.3 ms                                                | 68.0 ms: 1.40x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 934 ms: 1.40x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 459 ms: 1.40x faster                                                   |
| pycparser                | 877 ms                                                 | 631 ms: 1.39x faster                                                   |
| unpickle_pure_python     | 194 us                                                 | 141 us: 1.38x faster                                                   |
| django_template          | 26.4 ms                                                | 19.3 ms: 1.37x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.1 ms: 1.36x faster                                                  |
| scimark_sor              | 128 ms                                                 | 94.9 ms: 1.35x faster                                                  |
| pyflate                  | 427 ms                                                 | 318 ms: 1.34x faster                                                   |
| sympy_sum                | 92.2 ms                                                | 69.0 ms: 1.34x faster                                                  |
| deepcopy                 | 272 us                                                 | 204 us: 1.33x faster                                                   |
| thrift                   | 572 us                                                 | 430 us: 1.33x faster                                                   |
| tornado_http             | 86.7 ms                                                | 65.5 ms: 1.33x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.18 ms: 1.31x faster                                                  |
| coroutines               | 20.7 ms                                                | 15.9 ms: 1.30x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.23 sec: 1.30x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.80 us: 1.29x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 27.4 ms: 1.29x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.27x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 36.9 ms: 1.26x faster                                                  |
| sympy_str                | 165 ms                                                 | 131 ms: 1.26x faster                                                   |
| scimark_fft              | 224 ms                                                 | 180 ms: 1.25x faster                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.76 ms: 1.24x faster                                                  |
| genshi_text              | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                  |
| fannkuch                 | 303 ms                                                 | 247 ms: 1.23x faster                                                   |
| gunicorn                 | 1.30 ms                                                | 1.06 ms: 1.22x faster                                                  |
| aiohttp                  | 1.22 ms                                                | 1.00 ms: 1.22x faster                                                  |
| nqueens                  | 63.8 ms                                                | 52.6 ms: 1.21x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.43 sec: 1.21x faster                                                 |
| 2to3                     | 192 ms                                                 | 159 ms: 1.20x faster                                                   |
| sympy_expand             | 269 ms                                                 | 225 ms: 1.19x faster                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 31.0 ms: 1.19x faster                                                  |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.46 sec: 1.17x faster                                                 |
| dask                     | 253 ms                                                 | 218 ms: 1.16x faster                                                   |
| sqlglot_normalize        | 190 ms                                                 | 165 ms: 1.15x faster                                                   |
| bench_thread_pool        | 527 us                                                 | 457 us: 1.15x faster                                                   |
| genshi_xml               | 33.8 ms                                                | 30.2 ms: 1.12x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.1 ms: 1.11x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 70.2 ms: 1.11x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.48 sec: 1.10x faster                                                 |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 105 ms: 1.02x faster                                                   |
| xml_etree_generate       | 53.5 ms                                                | 52.5 ms: 1.02x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 71.6 ms: 1.01x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                  |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.14 us: 1.04x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 900 us: 1.05x slower                                                   |
| regex_effbot             | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.05x slower                                                  |
| unpickle_list            | 2.69 us                                                | 2.88 us: 1.07x slower                                                  |
| pickle                   | 6.97 us                                                | 7.51 us: 1.08x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.9 ms: 1.08x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.6 us: 1.10x slower                                                  |
| pickle_list              | 2.74 us                                                | 3.02 us: 1.10x slower                                                  |
| flaskblogging            | 2.65 ms                                                | 3.10 ms: 1.17x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 45.3 ms: 1.21x slower                                                  |
| async_generators         | 231 ms                                                 | 282 ms: 1.22x slower                                                   |
| python_startup           | 10.9 ms                                                | 13.3 ms: 1.22x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 10.3 ms: 1.30x slower                                                  |
| telco                    | 3.49 ms                                                | 4.58 ms: 1.31x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (12) of results/bm-20240601-3.13.0b1+-edb6883/bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 0.78x