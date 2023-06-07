
# Results vs. 3.11.0

- fork: python
- ref: v3.11.4
- machine: darwin-arm64
- commit hash: d2340ef
- commit date: 2023-06-06
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 155 ms: 1.04x faster                                   |
| chameleon      | 4.60 ms                                                | 4.30 ms: 1.07x faster                                  |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.01x faster                                 |
| html5lib       | 34.7 ms                                                | 33.0 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 53.0 ms                                                | 55.4 ms: 1.05x slower                                  |
| nbody          | 65.6 ms                                                | 68.7 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.07x faster                                  |
| regex_v8       | 16.1 ms                                                | 15.1 ms: 1.07x faster                                  |
| regex_compile  | 76.7 ms                                                | 73.4 ms: 1.05x faster                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle             | 9.67 us                                                | 8.34 us: 1.16x faster                                  |
| tomli_loads          | 1.47 sec                                               | 1.32 sec: 1.11x faster                                 |
| pickle_list          | 2.81 us                                                | 2.64 us: 1.06x faster                                  |
| pickle_dict          | 18.0 us                                                | 17.0 us: 1.06x faster                                  |
| xml_etree_process    | 35.1 ms                                                | 34.1 ms: 1.03x faster                                  |
| xml_etree_generate   | 48.3 ms                                                | 47.1 ms: 1.02x faster                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 68.6 ms: 1.02x faster                                  |
| json_loads           | 16.1 us                                                | 15.8 us: 1.02x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                   |
| json_dumps           | 7.63 ms                                                | 7.58 ms: 1.01x faster                                  |
| unpickle_list        | 2.65 us                                                | 2.67 us: 1.01x slower                                  |
| pickle               | 7.15 us                                                | 7.28 us: 1.02x slower                                  |
| unpickle_pure_python | 159 us                                                 | 162 us: 1.02x slower                                   |
| pickle_pure_python   | 201 us                                                 | 213 us: 1.06x slower                                   |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 8.91 ms: 1.14x faster                                  |
| python_startup         | 12.4 ms                                                | 10.9 ms: 1.14x faster                                  |
| Geometric mean         | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 21.0 ms                                                | 19.7 ms: 1.07x faster                                  |
| genshi_xml      | 29.8 ms                                                | 28.6 ms: 1.04x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.8 ms: 1.04x faster                                  |
| mako            | 8.53 ms                                                | 8.30 ms: 1.03x faster                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle                 | 9.67 us                                                | 8.34 us: 1.16x faster                                  |
| python_startup_no_site   | 10.2 ms                                                | 8.91 ms: 1.14x faster                                  |
| python_startup           | 12.4 ms                                                | 10.9 ms: 1.14x faster                                  |
| tomli_loads              | 1.47 sec                                               | 1.32 sec: 1.11x faster                                 |
| deltablue                | 2.81 ms                                                | 2.55 ms: 1.10x faster                                  |
| nqueens                  | 59.8 ms                                                | 54.4 ms: 1.10x faster                                  |
| comprehensions           | 16.1 us                                                | 14.8 us: 1.09x faster                                  |
| sqlglot_parse            | 959 us                                                 | 881 us: 1.09x faster                                   |
| scimark_lu               | 73.3 ms                                                | 68.0 ms: 1.08x faster                                  |
| sqlglot_transpile        | 1.12 ms                                                | 1.04 ms: 1.08x faster                                  |
| scimark_fft              | 200 ms                                                 | 186 ms: 1.07x faster                                   |
| bench_mp_pool            | 43.9 ms                                                | 41.0 ms: 1.07x faster                                  |
| regex_effbot             | 2.63 ms                                                | 2.45 ms: 1.07x faster                                  |
| telco                    | 3.41 ms                                                | 3.18 ms: 1.07x faster                                  |
| crypto_pyaes             | 51.7 ms                                                | 48.3 ms: 1.07x faster                                  |
| coroutines               | 17.8 ms                                                | 16.6 ms: 1.07x faster                                  |
| chameleon                | 4.60 ms                                                | 4.30 ms: 1.07x faster                                  |
| django_template          | 21.0 ms                                                | 19.7 ms: 1.07x faster                                  |
| regex_v8                 | 16.1 ms                                                | 15.1 ms: 1.07x faster                                  |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 2.99 ms: 1.07x faster                                  |
| sqlglot_normalize        | 171 ms                                                 | 160 ms: 1.07x faster                                   |
| pickle_list              | 2.81 us                                                | 2.64 us: 1.06x faster                                  |
| fannkuch                 | 261 ms                                                 | 246 ms: 1.06x faster                                   |
| pylint                   | 272 ms                                                 | 257 ms: 1.06x faster                                   |
| pickle_dict              | 18.0 us                                                | 17.0 us: 1.06x faster                                  |
| html5lib                 | 34.7 ms                                                | 33.0 ms: 1.05x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 32.4 ns: 1.05x faster                                  |
| logging_silent           | 68.1 ns                                                | 64.8 ns: 1.05x faster                                  |
| sympy_sum                | 85.5 ms                                                | 81.4 ms: 1.05x faster                                  |
| sqlglot_optimize         | 31.1 ms                                                | 29.7 ms: 1.05x faster                                  |
| pycparser                | 698 ms                                                 | 667 ms: 1.05x faster                                   |
| regex_compile            | 76.7 ms                                                | 73.4 ms: 1.05x faster                                  |
| spectral_norm            | 72.6 ms                                                | 69.5 ms: 1.04x faster                                  |
| genshi_xml               | 29.8 ms                                                | 28.6 ms: 1.04x faster                                  |
| go                       | 109 ms                                                 | 104 ms: 1.04x faster                                   |
| sympy_str                | 151 ms                                                 | 145 ms: 1.04x faster                                   |
| 2to3                     | 161 ms                                                 | 155 ms: 1.04x faster                                   |
| scimark_monte_carlo      | 46.5 ms                                                | 44.7 ms: 1.04x faster                                  |
| thrift                   | 442 us                                                 | 426 us: 1.04x faster                                   |
| genshi_text              | 15.3 ms                                                | 14.8 ms: 1.04x faster                                  |
| bench_thread_pool        | 474 us                                                 | 459 us: 1.03x faster                                   |
| sqlalchemy_declarative   | 62.6 ms                                                | 60.6 ms: 1.03x faster                                  |
| typing_runtime_protocols | 336 us                                                 | 325 us: 1.03x faster                                   |
| hexiom                   | 4.72 ms                                                | 4.58 ms: 1.03x faster                                  |
| pyflate                  | 310 ms                                                 | 301 ms: 1.03x faster                                   |
| gunicorn                 | 1.11 ms                                                | 1.08 ms: 1.03x faster                                  |
| richards_super           | 39.2 ms                                                | 38.1 ms: 1.03x faster                                  |
| mako                     | 8.53 ms                                                | 8.30 ms: 1.03x faster                                  |
| xml_etree_process        | 35.1 ms                                                | 34.1 ms: 1.03x faster                                  |
| logging_simple           | 3.55 us                                                | 3.46 us: 1.03x faster                                  |
| scimark_sor              | 82.6 ms                                                | 80.5 ms: 1.03x faster                                  |
| sympy_expand             | 242 ms                                                 | 236 ms: 1.02x faster                                   |
| xml_etree_generate       | 48.3 ms                                                | 47.1 ms: 1.02x faster                                  |
| xml_etree_iterparse      | 70.1 ms                                                | 68.6 ms: 1.02x faster                                  |
| sympy_integrate          | 11.5 ms                                                | 11.3 ms: 1.02x faster                                  |
| chaos                    | 49.4 ms                                                | 48.4 ms: 1.02x faster                                  |
| regex_dna                | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 524 ms: 1.02x faster                                   |
| async_generators         | 196 ms                                                 | 193 ms: 1.02x faster                                   |
| json_loads               | 16.1 us                                                | 15.8 us: 1.02x faster                                  |
| richards                 | 32.2 ms                                                | 31.7 ms: 1.02x faster                                  |
| docutils                 | 1.47 sec                                               | 1.45 sec: 1.01x faster                                 |
| dulwich_log              | 30.3 ms                                                | 29.9 ms: 1.01x faster                                  |
| logging_format           | 3.78 us                                                | 3.73 us: 1.01x faster                                  |
| xml_etree_parse          | 108 ms                                                 | 107 ms: 1.01x faster                                   |
| raytrace                 | 207 ms                                                 | 205 ms: 1.01x faster                                   |
| json_dumps               | 7.63 ms                                                | 7.58 ms: 1.01x faster                                  |
| sqlalchemy_imperative    | 7.20 ms                                                | 7.23 ms: 1.00x slower                                  |
| async_tree_none          | 286 ms                                                 | 287 ms: 1.00x slower                                   |
| unpickle_list            | 2.65 us                                                | 2.67 us: 1.01x slower                                  |
| json                     | 2.78 ms                                                | 2.80 ms: 1.01x slower                                  |
| create_gc_cycles         | 716 us                                                 | 726 us: 1.01x slower                                   |
| pickle                   | 7.15 us                                                | 7.28 us: 1.02x slower                                  |
| unpickle_pure_python     | 159 us                                                 | 162 us: 1.02x slower                                   |
| pprint_safe_repr         | 466 ms                                                 | 478 ms: 1.02x slower                                   |
| meteor_contest           | 73.5 ms                                                | 75.6 ms: 1.03x slower                                  |
| pprint_pformat           | 954 ms                                                 | 985 ms: 1.03x slower                                   |
| deepcopy_reduce          | 1.91 us                                                | 1.99 us: 1.04x slower                                  |
| float                    | 53.0 ms                                                | 55.4 ms: 1.05x slower                                  |
| nbody                    | 65.6 ms                                                | 68.7 ms: 1.05x slower                                  |
| async_tree_memoization   | 336 ms                                                 | 352 ms: 1.05x slower                                   |
| sqlite_synth             | 1.27 us                                                | 1.34 us: 1.05x slower                                  |
| deepcopy                 | 223 us                                                 | 234 us: 1.05x slower                                   |
| gc_traversal             | 2.42 ms                                                | 2.54 ms: 1.05x slower                                  |
| pickle_pure_python       | 201 us                                                 | 213 us: 1.06x slower                                   |
| deepcopy_memo            | 26.3 us                                                | 28.9 us: 1.10x slower                                  |
| mdp                      | 1.55 sec                                               | 1.74 sec: 1.13x slower                                 |
| pathlib                  | 27.2 ms                                                | 30.9 ms: 1.13x slower                                  |
| mypy2                    | 195 ms                                                 | 241 ms: 1.24x slower                                   |
| Geometric mean           | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (8): tornado_http, flaskblogging, asyncio_tcp_ssl, generators, pidigits, aiohttp, async_tree_io, asyncio_tcp
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: coverage
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230606-3.11.4-d2340ef/bm-20230606-darwin-arm64-python-v3.11.4-3.11.4-d2340ef.json: dask
