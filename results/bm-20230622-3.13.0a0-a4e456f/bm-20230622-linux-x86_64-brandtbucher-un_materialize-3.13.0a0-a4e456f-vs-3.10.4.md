
# Results vs. 3.10.4

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: a4e456f
- commit date: 2023-06-22
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.67 sec: 1.19x faster                                                |
| tornado_http   | 127 ms                                                 | 96.8 ms: 1.32x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.8 ms: 1.53x faster                                                 |
| float          | 111 ms                                                 | 79.9 ms: 1.38x faster                                                 |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                  |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                 |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.50 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 311 us: 1.46x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 214 us: 1.40x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.86 ms: 1.37x faster                                                 |
| tomli_loads          | 2.92 sec                                               | 2.21 sec: 1.32x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 58.7 ms: 1.28x faster                                                 |
| json_loads           | 28.8 us                                                | 25.1 us: 1.15x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 85.2 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 155 ms: 1.05x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.50 us: 1.01x faster                                                 |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.03x slower                                                 |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                 |
| unpickle             | 14.1 us                                                | 15.3 us: 1.08x slower                                                 |
| pickle_dict          | 27.3 us                                                | 31.2 us: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.17 ms: 1.54x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.67 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.37x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 150 us: 3.41x faster                                                  |
| generators               | 76.8 ms                                                | 29.3 ms: 2.62x faster                                                 |
| deltablue                | 7.42 ms                                                | 3.28 ms: 2.26x faster                                                 |
| chaos                    | 106 ms                                                 | 58.9 ms: 1.80x faster                                                 |
| asyncio_tcp              | 925 ms                                                 | 513 ms: 1.80x faster                                                  |
| richards_super           | 90.7 ms                                                | 51.7 ms: 1.76x faster                                                 |
| logging_silent           | 175 ns                                                 | 100 ns: 1.75x faster                                                  |
| raytrace                 | 464 ms                                                 | 273 ms: 1.70x faster                                                  |
| go                       | 229 ms                                                 | 136 ms: 1.68x faster                                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                |
| scimark_sor              | 197 ms                                                 | 119 ms: 1.65x faster                                                  |
| richards                 | 74.9 ms                                                | 45.6 ms: 1.64x faster                                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.30 ms: 1.58x faster                                                 |
| hexiom                   | 9.53 ms                                                | 6.12 ms: 1.56x faster                                                 |
| unpack_sequence          | 64.7 ns                                                | 41.8 ns: 1.55x faster                                                 |
| python_startup           | 14.2 ms                                                | 9.17 ms: 1.54x faster                                                 |
| crypto_pyaes             | 118 ms                                                 | 77.4 ms: 1.53x faster                                                 |
| nbody                    | 142 ms                                                 | 92.8 ms: 1.53x faster                                                 |
| scimark_monte_carlo      | 108 ms                                                 | 71.2 ms: 1.52x faster                                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                                 |
| pyflate                  | 673 ms                                                 | 448 ms: 1.50x faster                                                  |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.50x faster                                                  |
| async_tree_none          | 717 ms                                                 | 482 ms: 1.49x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                                |
| pickle_pure_python       | 455 us                                                 | 311 us: 1.46x faster                                                  |
| async_tree_memoization   | 854 ms                                                 | 589 ms: 1.45x faster                                                  |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.44x faster                                                  |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                 |
| unpickle_pure_python     | 300 us                                                 | 214 us: 1.40x faster                                                  |
| deepcopy_memo            | 52.3 us                                                | 37.6 us: 1.39x faster                                                 |
| float                    | 111 ms                                                 | 79.9 ms: 1.38x faster                                                 |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.37x faster                                                 |
| json_dumps               | 13.5 ms                                                | 9.86 ms: 1.37x faster                                                 |
| logging_format           | 8.91 us                                                | 6.49 us: 1.37x faster                                                 |
| logging_simple           | 8.07 us                                                | 5.93 us: 1.36x faster                                                 |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                |
| pprint_safe_repr         | 955 ms                                                 | 721 ms: 1.32x faster                                                  |
| tomli_loads              | 2.92 sec                                               | 2.21 sec: 1.32x faster                                                |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                |
| tornado_http             | 127 ms                                                 | 96.8 ms: 1.32x faster                                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 725 ms: 1.31x faster                                                  |
| regex_compile            | 177 ms                                                 | 135 ms: 1.31x faster                                                  |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.30x faster                                                 |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                                  |
| xml_etree_process        | 74.9 ms                                                | 58.7 ms: 1.28x faster                                                 |
| mypy2                    | 428 ms                                                 | 337 ms: 1.27x faster                                                  |
| deepcopy                 | 442 us                                                 | 351 us: 1.26x faster                                                  |
| nqueens                  | 100 ms                                                 | 79.5 ms: 1.26x faster                                                 |
| sqlglot_optimize         | 65.3 ms                                                | 52.4 ms: 1.25x faster                                                 |
| fannkuch                 | 486 ms                                                 | 398 ms: 1.22x faster                                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.17 us: 1.21x faster                                                 |
| scimark_fft              | 424 ms                                                 | 351 ms: 1.21x faster                                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.55 ms: 1.20x faster                                                 |
| docutils                 | 3.17 sec                                               | 2.67 sec: 1.19x faster                                                |
| bench_thread_pool        | 947 us                                                 | 822 us: 1.15x faster                                                  |
| dulwich_log              | 75.9 ms                                                | 66.0 ms: 1.15x faster                                                 |
| json_loads               | 28.8 us                                                | 25.1 us: 1.15x faster                                                 |
| regex_v8                 | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                 |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                                 |
| mdp                      | 2.82 sec                                               | 2.53 sec: 1.11x faster                                                |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                                 |
| xml_etree_generate       | 94.2 ms                                                | 85.2 ms: 1.11x faster                                                 |
| regex_dna                | 222 ms                                                 | 203 ms: 1.09x faster                                                  |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                  |
| sqlite_synth             | 2.93 us                                                | 2.75 us: 1.07x faster                                                 |
| pathlib                  | 20.0 ms                                                | 18.9 ms: 1.06x faster                                                 |
| xml_etree_parse          | 163 ms                                                 | 155 ms: 1.05x faster                                                  |
| pickle_list              | 4.56 us                                                | 4.50 us: 1.01x faster                                                 |
| pidigits                 | 190 ms                                                 | 192 ms: 1.01x slower                                                  |
| unpickle_list            | 4.82 us                                                | 4.94 us: 1.03x slower                                                 |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                                 |
| async_generators         | 425 ms                                                 | 447 ms: 1.05x slower                                                  |
| telco                    | 6.54 ms                                                | 6.88 ms: 1.05x slower                                                 |
| unpickle                 | 14.1 us                                                | 15.3 us: 1.08x slower                                                 |
| regex_effbot             | 3.23 ms                                                | 3.50 ms: 1.08x slower                                                 |
| gc_traversal             | 3.84 ms                                                | 4.31 ms: 1.12x slower                                                 |
| pickle_dict              | 27.3 us                                                | 31.2 us: 1.14x slower                                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.67 ms: 1.15x slower                                                 |
| dask                     | 423 ms                                                 | 519 ms: 1.23x slower                                                  |
| coverage                 | 72.8 ms                                                | 93.1 ms: 1.28x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
