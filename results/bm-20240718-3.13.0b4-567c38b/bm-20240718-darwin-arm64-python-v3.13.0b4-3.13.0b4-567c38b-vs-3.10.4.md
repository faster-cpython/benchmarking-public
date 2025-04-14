# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b4
- machine: darwin-arm64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.303x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 162 ms: 1.18x faster                                       |
| chameleon      | 6.26 ms                                                | 4.31 ms: 1.45x faster                                      |
| docutils       | 1.73 sec                                               | 1.45 sec: 1.20x faster                                     |
| html5lib       | 42.4 ms                                                | 31.5 ms: 1.35x faster                                      |
| tornado_http   | 86.7 ms                                                | 66.8 ms: 1.30x faster                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 210 ms: 1.85x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 260 ms: 1.82x faster                                       |
| async_tree_io           | 980 ms                                                 | 557 ms: 1.76x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 469 ms: 1.39x faster                                       |
| Geometric mean          | (ref)                                                  | 1.69x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.8 ms: 1.56x faster                                      |
| float          | 69.0 ms                                                | 48.7 ms: 1.42x faster                                      |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.30x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.4 ms: 1.39x faster                                      |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                       |
| regex_v8       | 17.1 ms                                                | 17.2 ms: 1.00x slower                                      |
| regex_effbot   | 2.46 ms                                                | 2.57 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 180 us: 1.56x faster                                       |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                       |
| json_dumps           | 8.11 ms                                                | 6.25 ms: 1.30x faster                                      |
| xml_etree_process    | 46.5 ms                                                | 37.3 ms: 1.25x faster                                      |
| tomli_loads          | 1.71 sec                                               | 1.48 sec: 1.16x faster                                     |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                       |
| xml_etree_iterparse  | 72.1 ms                                                | 71.3 ms: 1.01x faster                                      |
| xml_etree_generate   | 53.5 ms                                                | 53.0 ms: 1.01x faster                                      |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                      |
| Geometric mean       | (ref)                                                  | 1.17x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.1 ms: 1.30x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 11.3 ms: 1.43x slower                                      |
| Geometric mean         | (ref)                                                  | 1.36x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.00 ms: 1.41x faster                                      |
| django_template | 26.4 ms                                                | 19.5 ms: 1.35x faster                                      |
| genshi_text     | 17.3 ms                                                | 13.8 ms: 1.26x faster                                      |
| genshi_xml      | 33.8 ms                                                | 29.8 ms: 1.14x faster                                      |
| Geometric mean  | (ref)                                                  | 1.29x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 88.7 us: 3.64x faster                                      |
| deltablue                | 4.91 ms                                                | 2.15 ms: 2.28x faster                                      |
| raytrace                 | 301 ms                                                 | 148 ms: 2.03x faster                                       |
| logging_silent           | 117 ns                                                 | 60.1 ns: 1.95x faster                                      |
| chaos                    | 65.8 ms                                                | 34.7 ms: 1.90x faster                                      |
| async_tree_none          | 388 ms                                                 | 210 ms: 1.85x faster                                       |
| async_tree_memoization   | 474 ms                                                 | 260 ms: 1.82x faster                                       |
| async_tree_io            | 980 ms                                                 | 557 ms: 1.76x faster                                       |
| sqlglot_parse            | 1.24 ms                                                | 730 us: 1.70x faster                                       |
| richards_super           | 57.8 ms                                                | 34.3 ms: 1.69x faster                                      |
| comprehensions           | 16.9 us                                                | 10.2 us: 1.66x faster                                      |
| pylint                   | 277 ms                                                 | 170 ms: 1.63x faster                                       |
| sqlglot_transpile        | 1.44 ms                                                | 892 us: 1.62x faster                                       |
| richards                 | 48.7 ms                                                | 31.2 ms: 1.56x faster                                      |
| pickle_pure_python       | 281 us                                                 | 180 us: 1.56x faster                                       |
| nbody                    | 93.0 ms                                                | 59.8 ms: 1.56x faster                                      |
| scimark_lu               | 103 ms                                                 | 66.7 ms: 1.54x faster                                      |
| scimark_monte_carlo      | 65.6 ms                                                | 42.6 ms: 1.54x faster                                      |
| deepcopy_memo            | 34.7 us                                                | 22.7 us: 1.53x faster                                      |
| hexiom                   | 6.19 ms                                                | 4.07 ms: 1.52x faster                                      |
| go                       | 151 ms                                                 | 100 ms: 1.50x faster                                       |
| asyncio_tcp              | 659 ms                                                 | 445 ms: 1.48x faster                                       |
| chameleon                | 6.26 ms                                                | 4.31 ms: 1.45x faster                                      |
| crypto_pyaes             | 71.8 ms                                                | 50.0 ms: 1.44x faster                                      |
| logging_simple           | 4.45 us                                                | 3.11 us: 1.43x faster                                      |
| logging_format           | 4.83 us                                                | 3.40 us: 1.42x faster                                      |
| spectral_norm            | 94.8 ms                                                | 66.8 ms: 1.42x faster                                      |
| float                    | 69.0 ms                                                | 48.7 ms: 1.42x faster                                      |
| mako                     | 9.87 ms                                                | 7.00 ms: 1.41x faster                                      |
| generators               | 32.3 ms                                                | 23.0 ms: 1.41x faster                                      |
| pprint_safe_repr         | 641 ms                                                 | 459 ms: 1.40x faster                                       |
| pprint_pformat           | 1.30 sec                                               | 936 ms: 1.39x faster                                       |
| regex_compile            | 95.3 ms                                                | 68.4 ms: 1.39x faster                                      |
| pycparser                | 877 ms                                                 | 630 ms: 1.39x faster                                       |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 469 ms: 1.39x faster                                       |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                       |
| mypy2                    | 607 ms                                                 | 447 ms: 1.36x faster                                       |
| django_template          | 26.4 ms                                                | 19.5 ms: 1.35x faster                                      |
| scimark_sor              | 128 ms                                                 | 95.0 ms: 1.35x faster                                      |
| html5lib                 | 42.4 ms                                                | 31.5 ms: 1.35x faster                                      |
| deepcopy                 | 272 us                                                 | 204 us: 1.33x faster                                       |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                       |
| sympy_sum                | 92.2 ms                                                | 69.5 ms: 1.33x faster                                      |
| thrift                   | 572 us                                                 | 433 us: 1.32x faster                                       |
| coroutines               | 20.7 ms                                                | 15.9 ms: 1.30x faster                                      |
| tornado_http             | 86.7 ms                                                | 66.8 ms: 1.30x faster                                      |
| json_dumps               | 8.11 ms                                                | 6.25 ms: 1.30x faster                                      |
| dulwich_log              | 35.3 ms                                                | 27.4 ms: 1.29x faster                                      |
| deepcopy_reduce          | 2.33 us                                                | 1.82 us: 1.28x faster                                      |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.27x faster                                      |
| genshi_text              | 17.3 ms                                                | 13.8 ms: 1.26x faster                                      |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.27 sec: 1.26x faster                                     |
| sympy_str                | 165 ms                                                 | 132 ms: 1.26x faster                                       |
| xml_etree_process        | 46.5 ms                                                | 37.3 ms: 1.25x faster                                      |
| scimark_fft              | 224 ms                                                 | 181 ms: 1.24x faster                                       |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.80 ms: 1.22x faster                                      |
| nqueens                  | 63.8 ms                                                | 52.9 ms: 1.21x faster                                      |
| docutils                 | 1.73 sec                                               | 1.45 sec: 1.20x faster                                     |
| sympy_expand             | 269 ms                                                 | 225 ms: 1.20x faster                                       |
| sqlglot_optimize         | 36.8 ms                                                | 30.8 ms: 1.19x faster                                      |
| fannkuch                 | 303 ms                                                 | 254 ms: 1.19x faster                                       |
| 2to3                     | 192 ms                                                 | 162 ms: 1.18x faster                                       |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                       |
| mdp                      | 1.63 sec                                               | 1.41 sec: 1.16x faster                                     |
| tomli_loads              | 1.71 sec                                               | 1.48 sec: 1.16x faster                                     |
| dask                     | 253 ms                                                 | 220 ms: 1.15x faster                                       |
| sqlglot_normalize        | 190 ms                                                 | 166 ms: 1.15x faster                                       |
| bench_thread_pool        | 527 us                                                 | 460 us: 1.15x faster                                       |
| genshi_xml               | 33.8 ms                                                | 29.8 ms: 1.14x faster                                      |
| meteor_contest           | 77.7 ms                                                | 70.5 ms: 1.10x faster                                      |
| json                     | 3.08 ms                                                | 2.92 ms: 1.06x faster                                      |
| pathlib                  | 24.5 ms                                                | 23.7 ms: 1.04x faster                                      |
| xml_etree_parse          | 108 ms                                                 | 105 ms: 1.03x faster                                       |
| xml_etree_iterparse      | 72.1 ms                                                | 71.3 ms: 1.01x faster                                      |
| xml_etree_generate       | 53.5 ms                                                | 53.0 ms: 1.01x faster                                      |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                       |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                       |
| regex_v8                 | 17.1 ms                                                | 17.2 ms: 1.00x slower                                      |
| create_gc_cycles         | 860 us                                                 | 867 us: 1.01x slower                                       |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                      |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                      |
| regex_effbot             | 2.46 ms                                                | 2.57 ms: 1.05x slower                                      |
| coverage                 | 41.5 ms                                                | 45.0 ms: 1.09x slower                                      |
| async_generators         | 231 ms                                                 | 282 ms: 1.22x slower                                       |
| bench_mp_pool            | 37.4 ms                                                | 46.5 ms: 1.24x slower                                      |
| python_startup           | 10.9 ms                                                | 14.1 ms: 1.30x slower                                      |
| telco                    | 3.49 ms                                                | 4.63 ms: 1.33x slower                                      |
| python_startup_no_site   | 7.91 ms                                                | 11.3 ms: 1.43x slower                                      |
| Geometric mean           | (ref)                                                  | 1.30x faster                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.303x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.19x