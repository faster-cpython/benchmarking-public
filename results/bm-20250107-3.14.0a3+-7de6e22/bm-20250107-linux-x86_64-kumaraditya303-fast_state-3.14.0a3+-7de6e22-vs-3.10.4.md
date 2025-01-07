# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.430x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                 |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                               |
| html5lib       | 88.9 ms                                                | 60.9 ms: 1.46x faster                                                |
| Geometric mean | (ref)                                                  | 1.36x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 577 ms: 3.07x faster                                                 |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.83x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 322 ms: 2.70x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 484 ms: 2.10x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.65x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 117 ms                                                 | 73.6 ms: 1.59x faster                                                |
| nbody          | 154 ms                                                 | 97.2 ms: 1.58x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.37x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                |
| regex_v8       | 27.8 ms                                                | 26.4 ms: 1.05x faster                                                |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.56x faster                                               |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 96.6 ms: 1.20x faster                                                |
| json_loads           | 31.2 us                                                | 26.4 us: 1.18x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                |
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                |
| mako            | 16.3 ms                                                | 11.8 ms: 1.38x faster                                                |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 577 ms: 3.07x faster                                                 |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.83x faster                                                 |
| generators               | 80.1 ms                                                | 28.4 ms: 2.82x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 322 ms: 2.70x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.30 ms: 2.40x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 484 ms: 2.10x faster                                                 |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                                 |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                 |
| chaos                    | 115 ms                                                 | 60.7 ms: 1.90x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 31.3 us: 1.87x faster                                                |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                 |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                 |
| richards_super           | 94.7 ms                                                | 51.3 ms: 1.85x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 70.4 ms: 1.82x faster                                                |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                 |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                 |
| richards                 | 79.3 ms                                                | 44.9 ms: 1.77x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 68.2 ms: 1.73x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.65x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.31 ms: 1.65x faster                                                |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.64x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.62 us: 1.59x faster                                                |
| float                    | 117 ms                                                 | 73.6 ms: 1.59x faster                                                |
| nbody                    | 154 ms                                                 | 97.2 ms: 1.58x faster                                                |
| pyflate                  | 716 ms                                                 | 458 ms: 1.56x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.56x faster                                               |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                 |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                                |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                                |
| html5lib                 | 88.9 ms                                                | 60.9 ms: 1.46x faster                                                |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.42x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                                 |
| thrift                   | 1.07 ms                                                | 769 us: 1.39x faster                                                 |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.38x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.38x faster                                                 |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                 |
| scimark_fft              | 466 ms                                                 | 345 ms: 1.35x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.81 ms: 1.35x faster                                                |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 63.9 ms: 1.32x faster                                                |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.32x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 52.6 ms: 1.32x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                |
| nqueens                  | 106 ms                                                 | 82.0 ms: 1.29x faster                                                |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.27x faster                                                |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                               |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 96.6 ms: 1.20x faster                                                |
| json_loads               | 31.2 us                                                | 26.4 us: 1.18x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                |
| json                     | 5.69 ms                                                | 4.97 ms: 1.14x faster                                                |
| bench_thread_pool        | 986 us                                                 | 866 us: 1.14x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                               |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                |
| async_generators         | 444 ms                                                 | 420 ms: 1.06x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 26.4 ms: 1.05x faster                                                |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                 |
| coverage                 | 79.4 ms                                                | 82.7 ms: 1.04x slower                                                |
| mypy2                    | 894 ms                                                 | 949 ms: 1.06x slower                                                 |
| telco                    | 7.27 ms                                                | 7.84 ms: 1.08x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.93 ms: 1.36x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                         |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.430x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.27x