# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: darwin-arm64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.192x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 0.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 174 ms: 1.10x faster                                       |
| chameleon      | 6.26 ms                                                | 4.84 ms: 1.29x faster                                      |
| docutils       | 1.73 sec                                               | 1.46 sec: 1.19x faster                                     |
| html5lib       | 42.4 ms                                                | 34.1 ms: 1.24x faster                                      |
| Geometric mean | (ref)                                                  | 1.17x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 253 ms: 1.53x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 332 ms: 1.43x faster                                       |
| async_tree_io           | 980 ms                                                 | 707 ms: 1.39x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 523 ms: 1.24x faster                                       |
| Geometric mean          | (ref)                                                  | 1.39x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 74.0 ms: 1.26x faster                                      |
| float          | 69.0 ms                                                | 56.7 ms: 1.22x faster                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 73.4 ms: 1.30x faster                                      |
| regex_dna      | 174 ms                                                 | 146 ms: 1.20x faster                                       |
| regex_v8       | 17.1 ms                                                | 17.1 ms: 1.00x faster                                      |
| regex_effbot   | 2.46 ms                                                | 2.49 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 196 us: 1.43x faster                                       |
| unpickle_pure_python | 194 us                                                 | 154 us: 1.26x faster                                       |
| json_dumps           | 8.11 ms                                                | 6.46 ms: 1.26x faster                                      |
| xml_etree_process    | 46.5 ms                                                | 39.7 ms: 1.17x faster                                      |
| tomli_loads          | 1.71 sec                                               | 1.54 sec: 1.11x faster                                     |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                      |
| unpickle             | 8.80 us                                                | 9.10 us: 1.03x slower                                      |
| pickle               | 6.97 us                                                | 7.32 us: 1.05x slower                                      |
| xml_etree_generate   | 53.5 ms                                                | 56.2 ms: 1.05x slower                                      |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                      |
| xml_etree_iterparse  | 72.1 ms                                                | 77.6 ms: 1.08x slower                                      |
| pickle_list          | 2.74 us                                                | 2.96 us: 1.08x slower                                      |
| unpickle_list        | 2.69 us                                                | 3.07 us: 1.14x slower                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.6 ms: 1.53x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 14.8 ms: 1.87x slower                                      |
| Geometric mean         | (ref)                                                  | 1.69x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.33 ms: 1.35x faster                                      |
| django_template | 26.4 ms                                                | 21.6 ms: 1.22x faster                                      |
| genshi_text     | 17.3 ms                                                | 15.7 ms: 1.10x faster                                      |
| genshi_xml      | 33.8 ms                                                | 33.5 ms: 1.01x faster                                      |
| Geometric mean  | (ref)                                                  | 1.16x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 72.2 us: 4.47x faster                                      |
| deltablue                | 4.91 ms                                                | 2.44 ms: 2.02x faster                                      |
| raytrace                 | 301 ms                                                 | 171 ms: 1.76x faster                                       |
| logging_silent           | 117 ns                                                 | 69.5 ns: 1.69x faster                                      |
| chaos                    | 65.8 ms                                                | 39.4 ms: 1.67x faster                                      |
| asyncio_tcp              | 659 ms                                                 | 406 ms: 1.62x faster                                       |
| pylint                   | 277 ms                                                 | 171 ms: 1.61x faster                                       |
| mypy2                    | 607 ms                                                 | 385 ms: 1.58x faster                                       |
| sqlglot_parse            | 1.24 ms                                                | 790 us: 1.57x faster                                       |
| async_tree_none          | 388 ms                                                 | 253 ms: 1.53x faster                                       |
| richards_super           | 57.8 ms                                                | 37.7 ms: 1.53x faster                                      |
| crypto_pyaes             | 71.8 ms                                                | 48.2 ms: 1.49x faster                                      |
| sqlglot_transpile        | 1.44 ms                                                | 968 us: 1.49x faster                                       |
| go                       | 151 ms                                                 | 105 ms: 1.44x faster                                       |
| richards                 | 48.7 ms                                                | 33.9 ms: 1.44x faster                                      |
| pickle_pure_python       | 281 us                                                 | 196 us: 1.43x faster                                       |
| async_tree_memoization   | 474 ms                                                 | 332 ms: 1.43x faster                                       |
| comprehensions           | 16.9 us                                                | 12.1 us: 1.40x faster                                      |
| unpack_sequence          | 39.0 ns                                                | 28.0 ns: 1.40x faster                                      |
| scimark_monte_carlo      | 65.6 ms                                                | 47.0 ms: 1.40x faster                                      |
| scimark_lu               | 103 ms                                                 | 74.2 ms: 1.39x faster                                      |
| async_tree_io            | 980 ms                                                 | 707 ms: 1.39x faster                                       |
| hexiom                   | 6.19 ms                                                | 4.56 ms: 1.36x faster                                      |
| deepcopy_memo            | 34.7 us                                                | 25.7 us: 1.35x faster                                      |
| mako                     | 9.87 ms                                                | 7.33 ms: 1.35x faster                                      |
| logging_format           | 4.83 us                                                | 3.72 us: 1.30x faster                                      |
| regex_compile            | 95.3 ms                                                | 73.4 ms: 1.30x faster                                      |
| logging_simple           | 4.45 us                                                | 3.44 us: 1.29x faster                                      |
| chameleon                | 6.26 ms                                                | 4.84 ms: 1.29x faster                                      |
| spectral_norm            | 94.8 ms                                                | 74.4 ms: 1.27x faster                                      |
| sympy_sum                | 92.2 ms                                                | 72.4 ms: 1.27x faster                                      |
| pycparser                | 877 ms                                                 | 693 ms: 1.27x faster                                       |
| thrift                   | 572 us                                                 | 453 us: 1.26x faster                                       |
| unpickle_pure_python     | 194 us                                                 | 154 us: 1.26x faster                                       |
| pyflate                  | 427 ms                                                 | 339 ms: 1.26x faster                                       |
| nbody                    | 93.0 ms                                                | 74.0 ms: 1.26x faster                                      |
| json_dumps               | 8.11 ms                                                | 6.46 ms: 1.26x faster                                      |
| pprint_pformat           | 1.30 sec                                               | 1.05 sec: 1.25x faster                                     |
| pprint_safe_repr         | 641 ms                                                 | 514 ms: 1.25x faster                                       |
| html5lib                 | 42.4 ms                                                | 34.1 ms: 1.24x faster                                      |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 523 ms: 1.24x faster                                       |
| sympy_integrate          | 13.1 ms                                                | 10.7 ms: 1.23x faster                                      |
| django_template          | 26.4 ms                                                | 21.6 ms: 1.22x faster                                      |
| scimark_sor              | 128 ms                                                 | 105 ms: 1.22x faster                                       |
| float                    | 69.0 ms                                                | 56.7 ms: 1.22x faster                                      |
| deepcopy                 | 272 us                                                 | 224 us: 1.21x faster                                       |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.32 sec: 1.21x faster                                     |
| create_gc_cycles         | 860 us                                                 | 710 us: 1.21x faster                                       |
| dulwich_log              | 35.3 ms                                                | 29.4 ms: 1.20x faster                                      |
| sympy_str                | 165 ms                                                 | 138 ms: 1.20x faster                                       |
| regex_dna                | 174 ms                                                 | 146 ms: 1.20x faster                                       |
| docutils                 | 1.73 sec                                               | 1.46 sec: 1.19x faster                                     |
| deepcopy_reduce          | 2.33 us                                                | 1.97 us: 1.18x faster                                      |
| xml_etree_process        | 46.5 ms                                                | 39.7 ms: 1.17x faster                                      |
| generators               | 32.3 ms                                                | 28.6 ms: 1.13x faster                                      |
| sympy_expand             | 269 ms                                                 | 238 ms: 1.13x faster                                       |
| fannkuch                 | 303 ms                                                 | 268 ms: 1.13x faster                                       |
| tomli_loads              | 1.71 sec                                               | 1.54 sec: 1.11x faster                                     |
| scimark_fft              | 224 ms                                                 | 203 ms: 1.11x faster                                       |
| genshi_text              | 17.3 ms                                                | 15.7 ms: 1.10x faster                                      |
| 2to3                     | 192 ms                                                 | 174 ms: 1.10x faster                                       |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.12 ms: 1.10x faster                                      |
| sqlglot_optimize         | 36.8 ms                                                | 33.7 ms: 1.09x faster                                      |
| bench_thread_pool        | 527 us                                                 | 484 us: 1.09x faster                                       |
| coroutines               | 20.7 ms                                                | 19.2 ms: 1.08x faster                                      |
| meteor_contest           | 77.7 ms                                                | 72.9 ms: 1.07x faster                                      |
| nqueens                  | 63.8 ms                                                | 60.1 ms: 1.06x faster                                      |
| sqlglot_normalize        | 190 ms                                                 | 181 ms: 1.05x faster                                       |
| mdp                      | 1.63 sec                                               | 1.56 sec: 1.05x faster                                     |
| json                     | 3.08 ms                                                | 2.97 ms: 1.04x faster                                      |
| genshi_xml               | 33.8 ms                                                | 33.5 ms: 1.01x faster                                      |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                       |
| regex_v8                 | 17.1 ms                                                | 17.1 ms: 1.00x faster                                      |
| regex_effbot             | 2.46 ms                                                | 2.49 ms: 1.01x slower                                      |
| gc_traversal             | 2.36 ms                                                | 2.40 ms: 1.02x slower                                      |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                      |
| unpickle                 | 8.80 us                                                | 9.10 us: 1.03x slower                                      |
| pathlib                  | 24.5 ms                                                | 25.4 ms: 1.04x slower                                      |
| pickle                   | 6.97 us                                                | 7.32 us: 1.05x slower                                      |
| xml_etree_generate       | 53.5 ms                                                | 56.2 ms: 1.05x slower                                      |
| aiohttp                  | 1.22 ms                                                | 1.30 ms: 1.06x slower                                      |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 77.6 ms: 1.08x slower                                      |
| pickle_list              | 2.74 us                                                | 2.96 us: 1.08x slower                                      |
| sqlite_synth             | 1.46 us                                                | 1.60 us: 1.09x slower                                      |
| unpickle_list            | 2.69 us                                                | 3.07 us: 1.14x slower                                      |
| coverage                 | 41.5 ms                                                | 47.7 ms: 1.15x slower                                      |
| telco                    | 3.49 ms                                                | 4.47 ms: 1.28x slower                                      |
| async_generators         | 231 ms                                                 | 297 ms: 1.28x slower                                       |
| bench_mp_pool            | 37.4 ms                                                | 48.7 ms: 1.30x slower                                      |
| python_startup           | 10.9 ms                                                | 16.6 ms: 1.53x slower                                      |
| flaskblogging            | 2.65 ms                                                | 4.13 ms: 1.56x slower                                      |
| python_startup_no_site   | 7.91 ms                                                | 14.8 ms: 1.87x slower                                      |
| Geometric mean           | (ref)                                                  | 1.18x faster                                               |

Benchmark hidden because not significant (4): tornado_http, xml_etree_parse, pidigits, gunicorn
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.192x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 0.56x