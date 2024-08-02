# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: darwin-arm64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 0.69x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.19x faster                                                   |
| chameleon      | 6.26 ms                                                | 4.33 ms: 1.44x faster                                                  |
| docutils       | 1.73 sec                                               | 1.44 sec: 1.21x faster                                                 |
| html5lib       | 42.4 ms                                                | 31.2 ms: 1.36x faster                                                  |
| tornado_http   | 86.7 ms                                                | 65.8 ms: 1.32x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 207 ms: 1.88x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 255 ms: 1.85x faster                                                   |
| async_tree_io           | 980 ms                                                 | 552 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 464 ms: 1.40x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.7 ms: 1.56x faster                                                  |
| float          | 69.0 ms                                                | 48.3 ms: 1.43x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.3 ms: 1.40x faster                                                  |
| regex_dna      | 174 ms                                                 | 151 ms: 1.16x faster                                                   |
| regex_v8       | 17.1 ms                                                | 17.2 ms: 1.01x slower                                                  |
| regex_effbot   | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 179 us: 1.57x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 141 us: 1.38x faster                                                   |
| json_dumps           | 8.11 ms                                                | 6.21 ms: 1.30x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 36.9 ms: 1.26x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.03x faster                                                   |
| xml_etree_generate   | 53.5 ms                                                | 52.5 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 71.1 ms: 1.01x faster                                                  |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| unpickle             | 8.80 us                                                | 9.13 us: 1.04x slower                                                  |
| pickle               | 6.97 us                                                | 7.46 us: 1.07x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                  |
| unpickle_list        | 2.69 us                                                | 2.91 us: 1.08x slower                                                  |
| pickle_list          | 2.74 us                                                | 2.99 us: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.4 ms: 1.32x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 11.5 ms: 1.45x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.39x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.00 ms: 1.41x faster                                                  |
| django_template | 26.4 ms                                                | 19.4 ms: 1.36x faster                                                  |
| genshi_text     | 17.3 ms                                                | 13.8 ms: 1.25x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 30.1 ms: 1.12x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 88.0 us: 3.67x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.14 ms: 2.29x faster                                                  |
| raytrace                 | 301 ms                                                 | 147 ms: 2.05x faster                                                   |
| logging_silent           | 117 ns                                                 | 60.3 ns: 1.94x faster                                                  |
| chaos                    | 65.8 ms                                                | 34.1 ms: 1.93x faster                                                  |
| async_tree_none          | 388 ms                                                 | 207 ms: 1.88x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 255 ms: 1.85x faster                                                   |
| async_tree_io            | 980 ms                                                 | 552 ms: 1.77x faster                                                   |
| sqlglot_parse            | 1.24 ms                                                | 732 us: 1.70x faster                                                   |
| comprehensions           | 16.9 us                                                | 10.2 us: 1.67x faster                                                  |
| pylint                   | 277 ms                                                 | 167 ms: 1.65x faster                                                   |
| richards_super           | 57.8 ms                                                | 35.3 ms: 1.64x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 891 us: 1.62x faster                                                   |
| mypy2                    | 607 ms                                                 | 376 ms: 1.61x faster                                                   |
| pickle_pure_python       | 281 us                                                 | 179 us: 1.57x faster                                                   |
| nbody                    | 93.0 ms                                                | 59.7 ms: 1.56x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 423 ms: 1.56x faster                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 42.5 ms: 1.54x faster                                                  |
| scimark_lu               | 103 ms                                                 | 66.7 ms: 1.54x faster                                                  |
| richards                 | 48.7 ms                                                | 31.7 ms: 1.53x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 22.7 us: 1.53x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.07 ms: 1.52x faster                                                  |
| go                       | 151 ms                                                 | 100 ms: 1.50x faster                                                   |
| logging_simple           | 4.45 us                                                | 3.05 us: 1.46x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 49.4 ms: 1.45x faster                                                  |
| logging_format           | 4.83 us                                                | 3.32 us: 1.45x faster                                                  |
| chameleon                | 6.26 ms                                                | 4.33 ms: 1.44x faster                                                  |
| float                    | 69.0 ms                                                | 48.3 ms: 1.43x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 66.5 ms: 1.43x faster                                                  |
| generators               | 32.3 ms                                                | 22.8 ms: 1.42x faster                                                  |
| mako                     | 9.87 ms                                                | 7.00 ms: 1.41x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 464 ms: 1.40x faster                                                   |
| regex_compile            | 95.3 ms                                                | 68.3 ms: 1.40x faster                                                  |
| pycparser                | 877 ms                                                 | 633 ms: 1.39x faster                                                   |
| unpickle_pure_python     | 194 us                                                 | 141 us: 1.38x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 466 ms: 1.37x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 949 ms: 1.37x faster                                                   |
| django_template          | 26.4 ms                                                | 19.4 ms: 1.36x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.2 ms: 1.36x faster                                                  |
| scimark_sor              | 128 ms                                                 | 94.9 ms: 1.35x faster                                                  |
| pyflate                  | 427 ms                                                 | 319 ms: 1.34x faster                                                   |
| sympy_sum                | 92.2 ms                                                | 69.0 ms: 1.34x faster                                                  |
| deepcopy                 | 272 us                                                 | 204 us: 1.33x faster                                                   |
| thrift                   | 572 us                                                 | 432 us: 1.32x faster                                                   |
| tornado_http             | 86.7 ms                                                | 65.8 ms: 1.32x faster                                                  |
| coroutines               | 20.7 ms                                                | 15.9 ms: 1.30x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.21 ms: 1.30x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.23 sec: 1.30x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 27.5 ms: 1.28x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.82 us: 1.28x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 10.4 ms: 1.27x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 36.9 ms: 1.26x faster                                                  |
| genshi_text              | 17.3 ms                                                | 13.8 ms: 1.25x faster                                                  |
| sympy_str                | 165 ms                                                 | 132 ms: 1.25x faster                                                   |
| scimark_fft              | 224 ms                                                 | 181 ms: 1.24x faster                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.77 ms: 1.23x faster                                                  |
| fannkuch                 | 303 ms                                                 | 248 ms: 1.22x faster                                                   |
| nqueens                  | 63.8 ms                                                | 52.5 ms: 1.22x faster                                                  |
| aiohttp                  | 1.22 ms                                                | 1.01 ms: 1.21x faster                                                  |
| gunicorn                 | 1.30 ms                                                | 1.07 ms: 1.21x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.44 sec: 1.21x faster                                                 |
| 2to3                     | 192 ms                                                 | 160 ms: 1.19x faster                                                   |
| sympy_expand             | 269 ms                                                 | 226 ms: 1.19x faster                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 31.0 ms: 1.19x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.40 sec: 1.16x faster                                                 |
| dask                     | 253 ms                                                 | 218 ms: 1.16x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                 |
| regex_dna                | 174 ms                                                 | 151 ms: 1.16x faster                                                   |
| bench_thread_pool        | 527 us                                                 | 458 us: 1.15x faster                                                   |
| sqlglot_normalize        | 190 ms                                                 | 166 ms: 1.15x faster                                                   |
| genshi_xml               | 33.8 ms                                                | 30.1 ms: 1.12x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.0 ms: 1.11x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 70.3 ms: 1.11x faster                                                  |
| json                     | 3.08 ms                                                | 2.92 ms: 1.06x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 104 ms: 1.03x faster                                                   |
| xml_etree_generate       | 53.5 ms                                                | 52.5 ms: 1.02x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 71.1 ms: 1.01x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.2 ms: 1.01x slower                                                  |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.13 us: 1.04x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 898 us: 1.04x slower                                                   |
| regex_effbot             | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.55 us: 1.06x slower                                                  |
| pickle                   | 6.97 us                                                | 7.46 us: 1.07x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                  |
| unpickle_list            | 2.69 us                                                | 2.91 us: 1.08x slower                                                  |
| coverage                 | 41.5 ms                                                | 45.0 ms: 1.09x slower                                                  |
| pickle_list              | 2.74 us                                                | 2.99 us: 1.09x slower                                                  |
| flaskblogging            | 2.65 ms                                                | 3.13 ms: 1.18x slower                                                  |
| async_generators         | 231 ms                                                 | 281 ms: 1.22x slower                                                   |
| bench_mp_pool            | 37.4 ms                                                | 46.9 ms: 1.25x slower                                                  |
| telco                    | 3.49 ms                                                | 4.61 ms: 1.32x slower                                                  |
| python_startup           | 10.9 ms                                                | 14.4 ms: 1.32x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 11.5 ms: 1.45x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (12) of results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 0.69x