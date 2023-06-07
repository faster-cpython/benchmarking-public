
# Results vs. 3.10.4

- fork: python
- ref: v3.11.4
- machine: darwin-arm64
- commit hash: d2340ef
- commit date: 2023-06-06
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 155 ms: 1.30x faster                                   |
| chameleon      | 5.84 ms                                                | 4.30 ms: 1.36x faster                                  |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.23x faster                                 |
| html5lib       | 44.1 ms                                                | 33.0 ms: 1.34x faster                                  |
| tornado_http   | 91.9 ms                                                | 70.3 ms: 1.31x faster                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 68.7 ms: 1.37x faster                                  |
| float          | 72.3 ms                                                | 55.4 ms: 1.31x faster                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.22x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 73.4 ms: 1.32x faster                                  |
| regex_v8       | 17.5 ms                                                | 15.1 ms: 1.16x faster                                  |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.45 ms: 1.00x slower                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 1.76 sec                                               | 1.32 sec: 1.34x faster                                 |
| pickle_pure_python   | 284 us                                                 | 213 us: 1.33x faster                                   |
| xml_etree_process    | 45.1 ms                                                | 34.1 ms: 1.32x faster                                  |
| unpickle_pure_python | 203 us                                                 | 162 us: 1.25x faster                                   |
| unpickle             | 9.77 us                                                | 8.34 us: 1.17x faster                                  |
| xml_etree_generate   | 54.3 ms                                                | 47.1 ms: 1.15x faster                                  |
| json_dumps           | 8.38 ms                                                | 7.58 ms: 1.11x faster                                  |
| pickle_list          | 2.83 us                                                | 2.64 us: 1.07x faster                                  |
| json_loads           | 16.9 us                                                | 15.8 us: 1.07x faster                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 68.6 ms: 1.06x faster                                  |
| pickle_dict          | 17.8 us                                                | 17.0 us: 1.05x faster                                  |
| pickle               | 7.36 us                                                | 7.28 us: 1.01x faster                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 10.9 ms: 1.15x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 8.91 ms: 1.09x faster                                  |
| Geometric mean         | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 27.3 ms                                                | 19.7 ms: 1.39x faster                                  |
| genshi_xml      | 37.6 ms                                                | 28.6 ms: 1.31x faster                                  |
| mako            | 10.5 ms                                                | 8.30 ms: 1.26x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.8 ms: 1.25x faster                                  |
| Geometric mean  | (ref)                                                  | 1.30x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue                | 5.15 ms                                                | 2.55 ms: 2.02x faster                                  |
| logging_silent           | 119 ns                                                 | 64.8 ns: 1.84x faster                                  |
| richards                 | 51.4 ms                                                | 31.7 ms: 1.62x faster                                  |
| scimark_lu               | 110 ms                                                 | 68.0 ms: 1.62x faster                                  |
| crypto_pyaes             | 78.0 ms                                                | 48.3 ms: 1.62x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 44.7 ms: 1.62x faster                                  |
| raytrace                 | 328 ms                                                 | 205 ms: 1.60x faster                                   |
| richards_super           | 60.7 ms                                                | 38.1 ms: 1.59x faster                                  |
| go                       | 165 ms                                                 | 104 ms: 1.58x faster                                   |
| scimark_sor              | 127 ms                                                 | 80.5 ms: 1.57x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 881 us: 1.51x faster                                   |
| pyflate                  | 453 ms                                                 | 301 ms: 1.51x faster                                   |
| sqlglot_transpile        | 1.54 ms                                                | 1.04 ms: 1.47x faster                                  |
| async_tree_io            | 1.02 sec                                               | 706 ms: 1.44x faster                                   |
| async_tree_none          | 402 ms                                                 | 287 ms: 1.40x faster                                   |
| async_tree_memoization   | 493 ms                                                 | 352 ms: 1.40x faster                                   |
| django_template          | 27.3 ms                                                | 19.7 ms: 1.39x faster                                  |
| spectral_norm            | 96.4 ms                                                | 69.5 ms: 1.39x faster                                  |
| chaos                    | 66.8 ms                                                | 48.4 ms: 1.38x faster                                  |
| hexiom                   | 6.32 ms                                                | 4.58 ms: 1.38x faster                                  |
| thrift                   | 586 us                                                 | 426 us: 1.38x faster                                   |
| pycparser                | 915 ms                                                 | 667 ms: 1.37x faster                                   |
| nbody                    | 94.1 ms                                                | 68.7 ms: 1.37x faster                                  |
| chameleon                | 5.84 ms                                                | 4.30 ms: 1.36x faster                                  |
| logging_format           | 5.01 us                                                | 3.73 us: 1.34x faster                                  |
| tomli_loads              | 1.76 sec                                               | 1.32 sec: 1.34x faster                                 |
| logging_simple           | 4.63 us                                                | 3.46 us: 1.34x faster                                  |
| html5lib                 | 44.1 ms                                                | 33.0 ms: 1.34x faster                                  |
| pickle_pure_python       | 284 us                                                 | 213 us: 1.33x faster                                   |
| xml_etree_process        | 45.1 ms                                                | 34.1 ms: 1.32x faster                                  |
| regex_compile            | 96.6 ms                                                | 73.4 ms: 1.32x faster                                  |
| genshi_xml               | 37.6 ms                                                | 28.6 ms: 1.31x faster                                  |
| tornado_http             | 91.9 ms                                                | 70.3 ms: 1.31x faster                                  |
| float                    | 72.3 ms                                                | 55.4 ms: 1.31x faster                                  |
| 2to3                     | 202 ms                                                 | 155 ms: 1.30x faster                                   |
| fannkuch                 | 317 ms                                                 | 246 ms: 1.29x faster                                   |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 524 ms: 1.28x faster                                   |
| mypy2                    | 308 ms                                                 | 241 ms: 1.28x faster                                   |
| sqlglot_optimize         | 38.0 ms                                                | 29.7 ms: 1.28x faster                                  |
| pprint_safe_repr         | 609 ms                                                 | 478 ms: 1.27x faster                                   |
| mako                     | 10.5 ms                                                | 8.30 ms: 1.26x faster                                  |
| pprint_pformat           | 1.24 sec                                               | 985 ms: 1.26x faster                                   |
| unpickle_pure_python     | 203 us                                                 | 162 us: 1.25x faster                                   |
| nqueens                  | 68.1 ms                                                | 54.4 ms: 1.25x faster                                  |
| sqlalchemy_imperative    | 9.03 ms                                                | 7.23 ms: 1.25x faster                                  |
| genshi_text              | 18.4 ms                                                | 14.8 ms: 1.25x faster                                  |
| scimark_fft              | 232 ms                                                 | 186 ms: 1.25x faster                                   |
| dulwich_log              | 37.1 ms                                                | 29.9 ms: 1.24x faster                                  |
| gunicorn                 | 1.34 ms                                                | 1.08 ms: 1.24x faster                                  |
| sqlalchemy_declarative   | 74.8 ms                                                | 60.6 ms: 1.23x faster                                  |
| docutils                 | 1.78 sec                                               | 1.45 sec: 1.23x faster                                 |
| aiohttp                  | 1.29 ms                                                | 1.05 ms: 1.23x faster                                  |
| sqlglot_normalize        | 197 ms                                                 | 160 ms: 1.23x faster                                   |
| coroutines               | 20.2 ms                                                | 16.6 ms: 1.22x faster                                  |
| create_gc_cycles         | 876 us                                                 | 726 us: 1.21x faster                                   |
| async_generators         | 233 ms                                                 | 193 ms: 1.21x faster                                   |
| comprehensions           | 17.7 us                                                | 14.8 us: 1.20x faster                                  |
| pylint                   | 307 ms                                                 | 257 ms: 1.19x faster                                   |
| bench_thread_pool        | 548 us                                                 | 459 us: 1.19x faster                                   |
| deepcopy_reduce          | 2.38 us                                                | 1.99 us: 1.19x faster                                  |
| deepcopy_memo            | 34.5 us                                                | 28.9 us: 1.19x faster                                  |
| unpack_sequence          | 38.7 ns                                                | 32.4 ns: 1.19x faster                                  |
| deepcopy                 | 278 us                                                 | 234 us: 1.19x faster                                   |
| sympy_integrate          | 13.4 ms                                                | 11.3 ms: 1.19x faster                                  |
| unpickle                 | 9.77 us                                                | 8.34 us: 1.17x faster                                  |
| sympy_expand             | 276 ms                                                 | 236 ms: 1.17x faster                                   |
| sympy_str                | 169 ms                                                 | 145 ms: 1.16x faster                                   |
| regex_v8                 | 17.5 ms                                                | 15.1 ms: 1.16x faster                                  |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 2.99 ms: 1.16x faster                                  |
| dask                     | 258 ms                                                 | 222 ms: 1.16x faster                                   |
| sympy_sum                | 94.3 ms                                                | 81.4 ms: 1.16x faster                                  |
| telco                    | 3.68 ms                                                | 3.18 ms: 1.16x faster                                  |
| python_startup           | 12.6 ms                                                | 10.9 ms: 1.15x faster                                  |
| xml_etree_generate       | 54.3 ms                                                | 47.1 ms: 1.15x faster                                  |
| generators               | 32.9 ms                                                | 28.7 ms: 1.15x faster                                  |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.44 sec: 1.14x faster                                 |
| flaskblogging            | 2.75 ms                                                | 2.41 ms: 1.14x faster                                  |
| json_dumps               | 8.38 ms                                                | 7.58 ms: 1.11x faster                                  |
| json                     | 3.10 ms                                                | 2.80 ms: 1.11x faster                                  |
| sqlite_synth             | 1.47 us                                                | 1.34 us: 1.10x faster                                  |
| python_startup_no_site   | 9.73 ms                                                | 8.91 ms: 1.09x faster                                  |
| regex_dna                | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| pickle_list              | 2.83 us                                                | 2.64 us: 1.07x faster                                  |
| json_loads               | 16.9 us                                                | 15.8 us: 1.07x faster                                  |
| xml_etree_iterparse      | 72.6 ms                                                | 68.6 ms: 1.06x faster                                  |
| typing_runtime_protocols | 344 us                                                 | 325 us: 1.06x faster                                   |
| pickle_dict              | 17.8 us                                                | 17.0 us: 1.05x faster                                  |
| meteor_contest           | 78.6 ms                                                | 75.6 ms: 1.04x faster                                  |
| asyncio_tcp              | 673 ms                                                 | 655 ms: 1.03x faster                                   |
| pickle                   | 7.36 us                                                | 7.28 us: 1.01x faster                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| regex_effbot             | 2.45 ms                                                | 2.45 ms: 1.00x slower                                  |
| mdp                      | 1.67 sec                                               | 1.74 sec: 1.04x slower                                 |
| gc_traversal             | 2.40 ms                                                | 2.54 ms: 1.06x slower                                  |
| pathlib                  | 28.8 ms                                                | 30.9 ms: 1.07x slower                                  |
| Geometric mean           | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (3): xml_etree_parse, bench_mp_pool, unpickle_list
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: coverage
