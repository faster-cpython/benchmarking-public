# Results vs. 3.10.4

- fork: python
- ref: 8c094c3095feb4de2efe
- machine: darwin-arm64
- commit hash: 8c094c3
- commit date: 2024-03-13
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 2.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 187 ms: 1.02x faster                                                   |
| chameleon      | 6.26 ms                                                | 4.87 ms: 1.28x faster                                                  |
| docutils       | 1.73 sec                                               | 1.53 sec: 1.13x faster                                                 |
| html5lib       | 42.4 ms                                                | 35.8 ms: 1.18x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 254 ms: 1.53x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 332 ms: 1.43x faster                                                   |
| async_tree_io           | 980 ms                                                 | 710 ms: 1.38x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 523 ms: 1.24x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.39x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 70.2 ms: 1.32x faster                                                  |
| float          | 69.0 ms                                                | 53.0 ms: 1.30x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 152 ms: 1.15x faster                                                   |
| regex_compile  | 95.3 ms                                                | 84.9 ms: 1.12x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.2 ms: 1.01x slower                                                  |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 196 us: 1.43x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 150 us: 1.29x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.36 sec: 1.26x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.47 ms: 1.25x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 39.0 ms: 1.19x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.02x faster                                                   |
| xml_etree_iterparse  | 72.1 ms                                                | 74.6 ms: 1.03x slower                                                  |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                  |
| unpickle             | 8.80 us                                                | 9.19 us: 1.04x slower                                                  |
| pickle               | 6.97 us                                                | 7.29 us: 1.05x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 56.8 ms: 1.06x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                  |
| pickle_list          | 2.74 us                                                | 2.98 us: 1.09x slower                                                  |
| unpickle_list        | 2.69 us                                                | 3.05 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.5 ms: 1.70x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 16.7 ms: 2.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.90x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.74 ms: 1.46x faster                                                  |
| django_template | 26.4 ms                                                | 21.9 ms: 1.21x faster                                                  |
| genshi_text     | 17.3 ms                                                | 15.8 ms: 1.10x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 36.9 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.16x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 71.7 us: 4.50x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.53 ms: 1.94x faster                                                  |
| chaos                    | 65.8 ms                                                | 40.4 ms: 1.63x faster                                                  |
| logging_silent           | 117 ns                                                 | 72.3 ns: 1.62x faster                                                  |
| pylint                   | 277 ms                                                 | 176 ms: 1.57x faster                                                   |
| raytrace                 | 301 ms                                                 | 192 ms: 1.57x faster                                                   |
| async_tree_none          | 388 ms                                                 | 254 ms: 1.53x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 47.7 ms: 1.51x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 831 us: 1.50x faster                                                   |
| asyncio_tcp              | 659 ms                                                 | 440 ms: 1.50x faster                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 44.2 ms: 1.48x faster                                                  |
| mako                     | 9.87 ms                                                | 6.74 ms: 1.46x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 196 us: 1.43x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 332 ms: 1.43x faster                                                   |
| sqlglot_transpile        | 1.44 ms                                                | 1.02 ms: 1.41x faster                                                  |
| richards_super           | 57.8 ms                                                | 41.5 ms: 1.39x faster                                                  |
| async_tree_io            | 980 ms                                                 | 710 ms: 1.38x faster                                                   |
| comprehensions           | 16.9 us                                                | 12.6 us: 1.34x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 26.2 us: 1.33x faster                                                  |
| nbody                    | 93.0 ms                                                | 70.2 ms: 1.32x faster                                                  |
| go                       | 151 ms                                                 | 115 ms: 1.32x faster                                                   |
| float                    | 69.0 ms                                                | 53.0 ms: 1.30x faster                                                  |
| richards                 | 48.7 ms                                                | 37.5 ms: 1.30x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 150 us: 1.29x faster                                                   |
| chameleon                | 6.26 ms                                                | 4.87 ms: 1.28x faster                                                  |
| logging_format           | 4.83 us                                                | 3.79 us: 1.27x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.50 us: 1.27x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 74.8 ms: 1.27x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.36 sec: 1.26x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.47 ms: 1.25x faster                                                  |
| pyflate                  | 427 ms                                                 | 343 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 523 ms: 1.24x faster                                                   |
| thrift                   | 572 us                                                 | 461 us: 1.24x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 519 ms: 1.23x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 1.06 sec: 1.23x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.31 sec: 1.22x faster                                                 |
| hexiom                   | 6.19 ms                                                | 5.13 ms: 1.21x faster                                                  |
| django_template          | 26.4 ms                                                | 21.9 ms: 1.21x faster                                                  |
| pycparser                | 877 ms                                                 | 727 ms: 1.21x faster                                                   |
| create_gc_cycles         | 860 us                                                 | 714 us: 1.21x faster                                                   |
| scimark_lu               | 103 ms                                                 | 85.7 ms: 1.20x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 39.0 ms: 1.19x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 77.7 ms: 1.19x faster                                                  |
| html5lib                 | 42.4 ms                                                | 35.8 ms: 1.18x faster                                                  |
| deepcopy                 | 272 us                                                 | 231 us: 1.18x faster                                                   |
| deepcopy_reduce          | 2.33 us                                                | 2.00 us: 1.16x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 30.6 ms: 1.15x faster                                                  |
| scimark_sor              | 128 ms                                                 | 111 ms: 1.15x faster                                                   |
| regex_dna                | 174 ms                                                 | 152 ms: 1.15x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 11.5 ms: 1.14x faster                                                  |
| coroutines               | 20.7 ms                                                | 18.1 ms: 1.14x faster                                                  |
| sympy_str                | 165 ms                                                 | 145 ms: 1.14x faster                                                   |
| generators               | 32.3 ms                                                | 28.5 ms: 1.13x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.53 sec: 1.13x faster                                                 |
| regex_compile            | 95.3 ms                                                | 84.9 ms: 1.12x faster                                                  |
| scimark_fft              | 224 ms                                                 | 200 ms: 1.12x faster                                                   |
| gunicorn                 | 1.30 ms                                                | 1.18 ms: 1.11x faster                                                  |
| dask                     | 253 ms                                                 | 229 ms: 1.11x faster                                                   |
| aiohttp                  | 1.22 ms                                                | 1.11 ms: 1.10x faster                                                  |
| genshi_text              | 17.3 ms                                                | 15.8 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.15 ms: 1.09x faster                                                  |
| sympy_expand             | 269 ms                                                 | 249 ms: 1.08x faster                                                   |
| sqlglot_normalize        | 190 ms                                                 | 182 ms: 1.04x faster                                                   |
| json                     | 3.08 ms                                                | 2.97 ms: 1.04x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 35.4 ms: 1.04x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 75.2 ms: 1.03x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 514 us: 1.03x faster                                                   |
| 2to3                     | 192 ms                                                 | 187 ms: 1.02x faster                                                   |
| xml_etree_parse          | 108 ms                                                 | 105 ms: 1.02x faster                                                   |
| mdp                      | 1.63 sec                                               | 1.62 sec: 1.01x faster                                                 |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| regex_v8                 | 17.1 ms                                                | 17.2 ms: 1.01x slower                                                  |
| nqueens                  | 63.8 ms                                                | 64.2 ms: 1.01x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.42 ms: 1.02x slower                                                  |
| pathlib                  | 24.5 ms                                                | 25.2 ms: 1.03x slower                                                  |
| fannkuch                 | 303 ms                                                 | 311 ms: 1.03x slower                                                   |
| xml_etree_iterparse      | 72.1 ms                                                | 74.6 ms: 1.03x slower                                                  |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.19 us: 1.04x slower                                                  |
| pickle                   | 6.97 us                                                | 7.29 us: 1.05x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 56.8 ms: 1.06x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.58 us: 1.08x slower                                                  |
| pickle_list              | 2.74 us                                                | 2.98 us: 1.09x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 36.9 ms: 1.09x slower                                                  |
| unpickle_list            | 2.69 us                                                | 3.05 us: 1.13x slower                                                  |
| coverage                 | 41.5 ms                                                | 47.9 ms: 1.15x slower                                                  |
| telco                    | 3.49 ms                                                | 4.58 ms: 1.31x slower                                                  |
| async_generators         | 231 ms                                                 | 313 ms: 1.35x slower                                                   |
| bench_mp_pool            | 37.4 ms                                                | 53.2 ms: 1.42x slower                                                  |
| python_startup           | 10.9 ms                                                | 18.5 ms: 1.70x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 16.7 ms: 2.12x slower                                                  |
| unpack_sequence          | 39.0 ns                                                | 114 ns: 2.92x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.14x faster                                                           |

Benchmark hidden because not significant (3): tornado_http, asyncio_websockets, mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240313-3.13.0a5+-8c094c3-JIT/bm-20240313-darwin-arm64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x


# Memory

- memory change: 2.07x