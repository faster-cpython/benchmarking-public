
# Results vs. 3.11.0

- fork: python
- ref: ed7c3ff15680c1939fad
- machine: darwin-arm64
- commit hash: ed7c3ff
- commit date: 2022-09-11
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 181 ms: 1.12x slower                                                   |
| chameleon      | 4.57 ms                                                | 4.63 ms: 1.01x slower                                                  |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 76.4 ms: 1.00x faster                                                  |
| regex_v8       | 16.2 ms                                                | 16.4 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|---------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse     | 106 ms                                                 | 99.5 ms: 1.07x faster                                                  |
| xml_etree_iterparse | 69.2 ms                                                | 65.7 ms: 1.05x faster                                                  |
| json_dumps          | 7.72 ms                                                | 7.58 ms: 1.02x faster                                                  |
| xml_etree_generate  | 48.8 ms                                                | 48.3 ms: 1.01x faster                                                  |
| xml_etree_process   | 35.2 ms                                                | 35.1 ms: 1.00x faster                                                  |
| unpickle_list       | 2.63 us                                                | 2.64 us: 1.00x slower                                                  |
| pickle_pure_python  | 199 us                                                 | 199 us: 1.00x slower                                                   |
| pickle_dict         | 17.9 us                                                | 18.0 us: 1.01x slower                                                  |
| json_loads          | 16.1 us                                                | 16.2 us: 1.01x slower                                                  |
| pickle              | 7.17 us                                                | 7.22 us: 1.01x slower                                                  |
| pickle_list         | 2.81 us                                                | 2.85 us: 1.02x slower                                                  |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.27 ms: 1.28x faster                                                  |
| python_startup         | 11.5 ms                                                | 9.21 ms: 1.25x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.39 ms: 1.01x faster                                                  |
| genshi_text     | 15.3 ms                                                | 15.2 ms: 1.00x faster                                                  |
| django_template | 21.0 ms                                                | 21.1 ms: 1.00x slower                                                  |
| genshi_xml      | 29.8 ms                                                | 30.1 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.8 ms: 1.33x faster                                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.27 ms: 1.28x faster                                                  |
| python_startup          | 11.5 ms                                                | 9.21 ms: 1.25x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 99.5 ms: 1.07x faster                                                  |
| flaskblogging           | 2.42 ms                                                | 2.28 ms: 1.06x faster                                                  |
| async_tree_memoization  | 336 ms                                                 | 317 ms: 1.06x faster                                                   |
| xml_etree_iterparse     | 69.2 ms                                                | 65.7 ms: 1.05x faster                                                  |
| nqueens                 | 61.8 ms                                                | 59.5 ms: 1.04x faster                                                  |
| bench_thread_pool       | 473 us                                                 | 458 us: 1.03x faster                                                   |
| dulwich_log             | 29.9 ms                                                | 29.0 ms: 1.03x faster                                                  |
| bench_mp_pool           | 43.2 ms                                                | 41.9 ms: 1.03x faster                                                  |
| gunicorn                | 1.13 ms                                                | 1.10 ms: 1.03x faster                                                  |
| pylint                  | 271 ms                                                 | 265 ms: 1.02x faster                                                   |
| json_dumps              | 7.72 ms                                                | 7.58 ms: 1.02x faster                                                  |
| logging_simple          | 3.50 us                                                | 3.45 us: 1.02x faster                                                  |
| logging_format          | 3.78 us                                                | 3.73 us: 1.01x faster                                                  |
| generators              | 28.8 ms                                                | 28.4 ms: 1.01x faster                                                  |
| unpack_sequence         | 33.6 ns                                                | 33.1 ns: 1.01x faster                                                  |
| mako                    | 8.49 ms                                                | 8.39 ms: 1.01x faster                                                  |
| async_tree_none         | 285 ms                                                 | 281 ms: 1.01x faster                                                   |
| async_tree_io           | 706 ms                                                 | 698 ms: 1.01x faster                                                   |
| xml_etree_generate      | 48.8 ms                                                | 48.3 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 529 ms: 1.01x faster                                                   |
| thrift                  | 433 us                                                 | 429 us: 1.01x faster                                                   |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.24 ms: 1.01x faster                                                  |
| deepcopy                | 224 us                                                 | 222 us: 1.01x faster                                                   |
| logging_silent          | 68.0 ns                                                | 67.5 ns: 1.01x faster                                                  |
| sympy_sum               | 86.0 ms                                                | 85.5 ms: 1.01x faster                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.11 ms: 1.01x faster                                                  |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                 |
| deepcopy_reduce         | 1.91 us                                                | 1.90 us: 1.01x faster                                                  |
| sympy_str               | 152 ms                                                 | 151 ms: 1.01x faster                                                   |
| sympy_expand            | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| coroutines              | 17.7 ms                                                | 17.6 ms: 1.00x faster                                                  |
| sqlglot_parse           | 957 us                                                 | 953 us: 1.00x faster                                                   |
| genshi_text             | 15.3 ms                                                | 15.2 ms: 1.00x faster                                                  |
| sqlalchemy_declarative  | 62.7 ms                                                | 62.4 ms: 1.00x faster                                                  |
| regex_compile           | 76.7 ms                                                | 76.4 ms: 1.00x faster                                                  |
| xml_etree_process       | 35.2 ms                                                | 35.1 ms: 1.00x faster                                                  |
| mdp                     | 1.54 sec                                               | 1.54 sec: 1.00x faster                                                 |
| chaos                   | 49.5 ms                                                | 49.3 ms: 1.00x faster                                                  |
| raytrace                | 207 ms                                                 | 207 ms: 1.00x faster                                                   |
| hexiom                  | 4.73 ms                                                | 4.72 ms: 1.00x faster                                                  |
| sqlglot_optimize        | 31.2 ms                                                | 31.2 ms: 1.00x slower                                                  |
| meteor_contest          | 73.8 ms                                                | 74.0 ms: 1.00x slower                                                  |
| scimark_lu              | 72.1 ms                                                | 72.3 ms: 1.00x slower                                                  |
| unpickle_list           | 2.63 us                                                | 2.64 us: 1.00x slower                                                  |
| pickle_pure_python      | 199 us                                                 | 199 us: 1.00x slower                                                   |
| django_template         | 21.0 ms                                                | 21.1 ms: 1.00x slower                                                  |
| pprint_pformat          | 950 ms                                                 | 954 ms: 1.00x slower                                                   |
| pprint_safe_repr        | 465 ms                                                 | 467 ms: 1.00x slower                                                   |
| deltablue               | 2.81 ms                                                | 2.82 ms: 1.00x slower                                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                  |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                                  |
| pyflate                 | 311 ms                                                 | 313 ms: 1.01x slower                                                   |
| pickle                  | 7.17 us                                                | 7.22 us: 1.01x slower                                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 46.8 ms: 1.01x slower                                                  |
| scimark_fft             | 199 ms                                                 | 201 ms: 1.01x slower                                                   |
| fannkuch                | 261 ms                                                 | 263 ms: 1.01x slower                                                   |
| genshi_xml              | 29.8 ms                                                | 30.1 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 3.24 ms: 1.01x slower                                                  |
| chameleon               | 4.57 ms                                                | 4.63 ms: 1.01x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.29 us: 1.02x slower                                                  |
| regex_v8                | 16.2 ms                                                | 16.4 ms: 1.02x slower                                                  |
| pickle_list             | 2.81 us                                                | 2.85 us: 1.02x slower                                                  |
| richards                | 32.2 ms                                                | 32.8 ms: 1.02x slower                                                  |
| json                    | 2.77 ms                                                | 2.83 ms: 1.02x slower                                                  |
| 2to3                    | 161 ms                                                 | 181 ms: 1.12x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (19): tornado_http, aiohttp, float, spectral_norm, regex_effbot, sympy_integrate, async_generators, pycparser, sqlglot_normalize, regex_dna, scimark_sor, deepcopy_memo, crypto_pyaes, nbody, unpickle_pure_python, telco, go, html5lib, unpickle
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp, comprehensions, coverage, create_gc_cycles, dask, gc_traversal, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220911-3.11.0rc2-ed7c3ff/bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff.json: mypy
