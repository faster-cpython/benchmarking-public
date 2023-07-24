
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: d87d67b
- commit date: 2023-07-23
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 267 ms: 1.26x faster                                   |
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                 |
| tornado_http   | 127 ms                                                 | 100 ms: 1.27x faster                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.8 ms: 1.61x faster                                  |
| float          | 111 ms                                                 | 78.8 ms: 1.40x faster                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 144 ms: 1.23x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.8 ms: 1.10x faster                                  |
| regex_dna      | 222 ms                                                 | 213 ms: 1.04x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.58 ms: 1.11x slower                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 311 us: 1.47x faster                                   |
| unpickle_pure_python | 300 us                                                 | 216 us: 1.39x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.75 ms: 1.39x faster                                  |
| tomli_loads          | 2.92 sec                                               | 2.20 sec: 1.33x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 58.7 ms: 1.28x faster                                  |
| json_loads           | 28.8 us                                                | 25.8 us: 1.12x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 84.8 ms: 1.11x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                   |
| pickle_list          | 4.56 us                                                | 4.69 us: 1.03x slower                                  |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                  |
| unpickle_list        | 4.82 us                                                | 5.14 us: 1.07x slower                                  |
| unpickle             | 14.1 us                                                | 15.1 us: 1.07x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.30 ms: 1.52x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.75 ms: 1.16x slower                                  |
| Geometric mean         | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-linux-x86_64-python-3.12-3.12.0b4+-d87d67b |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 149 us: 3.43x faster                                   |
| generators               | 76.8 ms                                                | 30.3 ms: 2.54x faster                                  |
| deltablue                | 7.42 ms                                                | 3.50 ms: 2.12x faster                                  |
| richards_super           | 90.7 ms                                                | 49.2 ms: 1.84x faster                                  |
| asyncio_tcp              | 925 ms                                                 | 510 ms: 1.81x faster                                   |
| logging_silent           | 175 ns                                                 | 99.1 ns: 1.77x faster                                  |
| richards                 | 74.9 ms                                                | 42.8 ms: 1.75x faster                                  |
| go                       | 229 ms                                                 | 135 ms: 1.70x faster                                   |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                 |
| chaos                    | 106 ms                                                 | 63.6 ms: 1.67x faster                                  |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.62x faster                                   |
| nbody                    | 142 ms                                                 | 87.8 ms: 1.61x faster                                  |
| hexiom                   | 9.53 ms                                                | 6.08 ms: 1.57x faster                                  |
| raytrace                 | 464 ms                                                 | 297 ms: 1.56x faster                                   |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.54x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 77.1 ms: 1.54x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.53x faster                                 |
| python_startup           | 14.2 ms                                                | 9.30 ms: 1.52x faster                                  |
| async_tree_none          | 717 ms                                                 | 472 ms: 1.52x faster                                   |
| pyflate                  | 673 ms                                                 | 444 ms: 1.52x faster                                   |
| scimark_monte_carlo      | 108 ms                                                 | 71.7 ms: 1.51x faster                                  |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.49x faster                                   |
| async_tree_memoization   | 854 ms                                                 | 574 ms: 1.49x faster                                   |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.49x faster                                  |
| pickle_pure_python       | 455 us                                                 | 311 us: 1.47x faster                                   |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.43x faster                                   |
| coroutines               | 31.8 ms                                                | 22.5 ms: 1.42x faster                                  |
| float                    | 111 ms                                                 | 78.8 ms: 1.40x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 216 us: 1.39x faster                                   |
| deepcopy_memo            | 52.3 us                                                | 37.6 us: 1.39x faster                                  |
| json_dumps               | 13.5 ms                                                | 9.75 ms: 1.39x faster                                  |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 711 ms: 1.34x faster                                   |
| tomli_loads              | 2.92 sec                                               | 2.20 sec: 1.33x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.33x faster                                 |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.30x faster                                 |
| logging_format           | 8.91 us                                                | 6.85 us: 1.30x faster                                  |
| pprint_safe_repr         | 955 ms                                                 | 736 ms: 1.30x faster                                   |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.29x faster                                  |
| logging_simple           | 8.07 us                                                | 6.27 us: 1.29x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 58.7 ms: 1.28x faster                                  |
| tornado_http             | 127 ms                                                 | 100 ms: 1.27x faster                                   |
| 2to3                     | 336 ms                                                 | 267 ms: 1.26x faster                                   |
| sqlglot_normalize        | 135 ms                                                 | 108 ms: 1.26x faster                                   |
| mypy2                    | 428 ms                                                 | 343 ms: 1.25x faster                                   |
| fannkuch                 | 486 ms                                                 | 390 ms: 1.25x faster                                   |
| deepcopy                 | 442 us                                                 | 355 us: 1.25x faster                                   |
| nqueens                  | 100 ms                                                 | 81.1 ms: 1.23x faster                                  |
| unpack_sequence          | 64.7 ns                                                | 52.7 ns: 1.23x faster                                  |
| regex_compile            | 177 ms                                                 | 144 ms: 1.23x faster                                   |
| sqlglot_optimize         | 65.3 ms                                                | 53.6 ms: 1.22x faster                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.18 us: 1.20x faster                                  |
| scimark_fft              | 424 ms                                                 | 362 ms: 1.17x faster                                   |
| docutils                 | 3.17 sec                                               | 2.71 sec: 1.17x faster                                 |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.3 ms: 1.16x faster                                  |
| sqlalchemy_declarative   | 165 ms                                                 | 144 ms: 1.15x faster                                   |
| bench_thread_pool        | 947 us                                                 | 828 us: 1.14x faster                                   |
| dulwich_log              | 75.9 ms                                                | 67.8 ms: 1.12x faster                                  |
| json_loads               | 28.8 us                                                | 25.8 us: 1.12x faster                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.90 ms: 1.11x faster                                  |
| xml_etree_generate       | 94.2 ms                                                | 84.8 ms: 1.11x faster                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                  |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.11x faster                                 |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.11x faster                                   |
| pathlib                  | 20.0 ms                                                | 18.2 ms: 1.10x faster                                  |
| regex_v8                 | 25.0 ms                                                | 22.8 ms: 1.10x faster                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.09x faster                                   |
| json                     | 5.42 ms                                                | 4.99 ms: 1.09x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                   |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                  |
| regex_dna                | 222 ms                                                 | 213 ms: 1.04x faster                                   |
| pickle_list              | 4.56 us                                                | 4.69 us: 1.03x slower                                  |
| gc_traversal             | 3.84 ms                                                | 3.96 ms: 1.03x slower                                  |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                  |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| telco                    | 6.54 ms                                                | 6.84 ms: 1.05x slower                                  |
| async_generators         | 425 ms                                                 | 447 ms: 1.05x slower                                   |
| unpickle_list            | 4.82 us                                                | 5.14 us: 1.07x slower                                  |
| unpickle                 | 14.1 us                                                | 15.1 us: 1.07x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.58 ms: 1.11x slower                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.75 ms: 1.16x slower                                  |
| pickle_dict              | 27.3 us                                                | 31.9 us: 1.17x slower                                  |
| dask                     | 423 ms                                                 | 536 ms: 1.27x slower                                   |
| coverage                 | 72.8 ms                                                | 93.6 ms: 1.29x slower                                  |
| Geometric mean           | (ref)                                                  | 1.28x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
