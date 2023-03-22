
# Results vs. 3.10.4

- fork: python
- ref: 1dd9be6584413fbfa823
- machine: darwin-arm64
- commit hash: 1dd9be6
- commit date: 2022-12-06
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 223 ms: 1.11x slower                                                |
| chameleon      | 5.79 ms                                                | 5.83 ms: 1.01x slower                                               |
| docutils       | 1.78 sec                                               | 1.77 sec: 1.01x faster                                              |
| html5lib       | 44.2 ms                                                | 46.5 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x slower                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 92.6 ms: 1.01x faster                                               |
| float          | 72.4 ms                                                | 72.1 ms: 1.00x faster                                               |
| pidigits       | 282 ms                                                 | 284 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 17.6 ms                                                | 18.3 ms: 1.04x slower                                               |
| regex_effbot   | 2.46 ms                                                | 2.64 ms: 1.07x slower                                               |
| regex_dna      | 162 ms                                                 | 180 ms: 1.11x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x slower                                                        |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse     | 106 ms                                                 | 100 ms: 1.06x faster                                                |
| xml_etree_iterparse | 72.3 ms                                                | 69.0 ms: 1.05x faster                                               |
| json_dumps          | 8.40 ms                                                | 8.25 ms: 1.02x faster                                               |
| unpickle_list       | 2.69 us                                                | 2.66 us: 1.01x faster                                               |
| xml_etree_generate  | 54.2 ms                                                | 54.3 ms: 1.00x slower                                               |
| xml_etree_process   | 44.8 ms                                                | 44.9 ms: 1.00x slower                                               |
| json_loads          | 16.9 us                                                | 17.0 us: 1.01x slower                                               |
| pickle              | 7.35 us                                                | 7.56 us: 1.03x slower                                               |
| pickle_dict         | 17.9 us                                                | 18.8 us: 1.05x slower                                               |
| pickle_list         | 2.80 us                                                | 2.96 us: 1.05x slower                                               |
| Geometric mean      | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (3): unpickle_pure_python, unpickle, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.88 ms                                                | 6.95 ms: 1.28x faster                                               |
| python_startup         | 11.9 ms                                                | 9.57 ms: 1.24x faster                                               |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text    | 18.4 ms                                                | 18.2 ms: 1.01x faster                                               |
| genshi_xml     | 37.2 ms                                                | 37.3 ms: 1.01x slower                                               |
| mako           | 10.5 ms                                                | 10.7 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pathlib                 | 28.8 ms                                                | 22.0 ms: 1.31x faster                                               |
| python_startup_no_site  | 8.88 ms                                                | 6.95 ms: 1.28x faster                                               |
| python_startup          | 11.9 ms                                                | 9.57 ms: 1.24x faster                                               |
| gunicorn                | 1.35 ms                                                | 1.26 ms: 1.07x faster                                               |
| aiohttp                 | 1.27 ms                                                | 1.19 ms: 1.07x faster                                               |
| xml_etree_parse         | 106 ms                                                 | 100 ms: 1.06x faster                                                |
| flaskblogging           | 2.75 ms                                                | 2.60 ms: 1.06x faster                                               |
| bench_thread_pool       | 546 us                                                 | 518 us: 1.05x faster                                                |
| xml_etree_iterparse     | 72.3 ms                                                | 69.0 ms: 1.05x faster                                               |
| coverage                | 42.0 ms                                                | 40.6 ms: 1.04x faster                                               |
| sqlglot_parse           | 1.37 ms                                                | 1.33 ms: 1.02x faster                                               |
| pylint                  | 307 ms                                                 | 300 ms: 1.02x faster                                                |
| async_tree_memoization  | 490 ms                                                 | 481 ms: 1.02x faster                                                |
| json_dumps              | 8.40 ms                                                | 8.25 ms: 1.02x faster                                               |
| async_tree_io           | 1.02 sec                                               | 1.00 sec: 1.02x faster                                              |
| sqlglot_transpile       | 1.57 ms                                                | 1.55 ms: 1.02x faster                                               |
| deepcopy_reduce         | 2.37 us                                                | 2.34 us: 1.02x faster                                               |
| async_generators        | 234 ms                                                 | 231 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed | 669 ms                                                 | 661 ms: 1.01x faster                                                |
| genshi_text             | 18.4 ms                                                | 18.2 ms: 1.01x faster                                               |
| dulwich_log             | 37.1 ms                                                | 36.7 ms: 1.01x faster                                               |
| logging_silent          | 119 ns                                                 | 118 ns: 1.01x faster                                                |
| generators              | 32.7 ms                                                | 32.4 ms: 1.01x faster                                               |
| meteor_contest          | 78.1 ms                                                | 77.4 ms: 1.01x faster                                               |
| unpickle_list           | 2.69 us                                                | 2.66 us: 1.01x faster                                               |
| nbody                   | 93.3 ms                                                | 92.6 ms: 1.01x faster                                               |
| richards                | 51.4 ms                                                | 51.0 ms: 1.01x faster                                               |
| scimark_monte_carlo     | 72.5 ms                                                | 72.0 ms: 1.01x faster                                               |
| deepcopy                | 281 us                                                 | 280 us: 1.01x faster                                                |
| sqlalchemy_declarative  | 74.9 ms                                                | 74.5 ms: 1.01x faster                                               |
| docutils                | 1.78 sec                                               | 1.77 sec: 1.01x faster                                              |
| float                   | 72.4 ms                                                | 72.1 ms: 1.00x faster                                               |
| pprint_safe_repr        | 606 ms                                                 | 603 ms: 1.00x faster                                                |
| scimark_fft             | 230 ms                                                 | 230 ms: 1.00x faster                                                |
| crypto_pyaes            | 78.1 ms                                                | 77.9 ms: 1.00x faster                                               |
| hexiom                  | 6.32 ms                                                | 6.30 ms: 1.00x faster                                               |
| pprint_pformat          | 1.23 sec                                               | 1.23 sec: 1.00x faster                                              |
| sqlglot_optimize        | 38.0 ms                                                | 37.9 ms: 1.00x faster                                               |
| sqlglot_normalize       | 196 ms                                                 | 196 ms: 1.00x faster                                                |
| chaos                   | 66.7 ms                                                | 66.6 ms: 1.00x faster                                               |
| mdp                     | 1.66 sec                                               | 1.66 sec: 1.00x slower                                              |
| fannkuch                | 317 ms                                                 | 318 ms: 1.00x slower                                                |
| scimark_lu              | 109 ms                                                 | 110 ms: 1.00x slower                                                |
| xml_etree_generate      | 54.2 ms                                                | 54.3 ms: 1.00x slower                                               |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.46 ms: 1.00x slower                                               |
| xml_etree_process       | 44.8 ms                                                | 44.9 ms: 1.00x slower                                               |
| sympy_expand            | 275 ms                                                 | 276 ms: 1.00x slower                                                |
| spectral_norm           | 95.8 ms                                                | 96.2 ms: 1.00x slower                                               |
| logging_format          | 4.97 us                                                | 4.99 us: 1.00x slower                                               |
| sympy_str               | 169 ms                                                 | 170 ms: 1.00x slower                                                |
| pidigits                | 282 ms                                                 | 284 ms: 1.00x slower                                                |
| raytrace                | 325 ms                                                 | 327 ms: 1.00x slower                                                |
| genshi_xml              | 37.2 ms                                                | 37.3 ms: 1.01x slower                                               |
| chameleon               | 5.79 ms                                                | 5.83 ms: 1.01x slower                                               |
| json_loads              | 16.9 us                                                | 17.0 us: 1.01x slower                                               |
| sympy_integrate         | 13.3 ms                                                | 13.4 ms: 1.01x slower                                               |
| sqlalchemy_imperative   | 8.89 ms                                                | 8.96 ms: 1.01x slower                                               |
| sqlite_synth            | 1.47 us                                                | 1.49 us: 1.01x slower                                               |
| json                    | 3.08 ms                                                | 3.11 ms: 1.01x slower                                               |
| mako                    | 10.5 ms                                                | 10.7 ms: 1.02x slower                                               |
| sympy_sum               | 93.6 ms                                                | 95.4 ms: 1.02x slower                                               |
| pickle                  | 7.35 us                                                | 7.56 us: 1.03x slower                                               |
| bench_mp_pool           | 39.7 ms                                                | 40.8 ms: 1.03x slower                                               |
| regex_v8                | 17.6 ms                                                | 18.3 ms: 1.04x slower                                               |
| pickle_dict             | 17.9 us                                                | 18.8 us: 1.05x slower                                               |
| html5lib                | 44.2 ms                                                | 46.5 ms: 1.05x slower                                               |
| pickle_list             | 2.80 us                                                | 2.96 us: 1.05x slower                                               |
| regex_effbot            | 2.46 ms                                                | 2.64 ms: 1.07x slower                                               |
| 2to3                    | 201 ms                                                 | 223 ms: 1.11x slower                                                |
| regex_dna               | 162 ms                                                 | 180 ms: 1.11x slower                                                |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (19): async_tree_none, pycparser, unpickle_pure_python, unpickle, go, nqueens, coroutines, django_template, scimark_sor, pyflate, unpack_sequence, logging_simple, regex_compile, telco, deepcopy_memo, thrift, deltablue, pickle_pure_python, tornado_http
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221206-3.10.9-1dd9be6/bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6.json: mypy
