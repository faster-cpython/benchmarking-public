
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 236cdad
- commit date: 2023-08-05
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 268 ms: 1.25x faster                                   |
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                 |
| tornado_http   | 127 ms                                                 | 99.3 ms: 1.28x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.9 ms: 1.58x faster                                  |
| float          | 111 ms                                                 | 80.6 ms: 1.37x faster                                  |
| pidigits       | 190 ms                                                 | 200 ms: 1.06x slower                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                  |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.54 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 309 us: 1.47x faster                                   |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.39x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.84 ms: 1.38x faster                                  |
| tomli_loads          | 2.92 sec                                               | 2.20 sec: 1.32x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 59.3 ms: 1.26x faster                                  |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 85.2 ms: 1.11x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                   |
| pickle_list          | 4.56 us                                                | 4.61 us: 1.01x slower                                  |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                  |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                  |
| unpickle             | 14.1 us                                                | 15.8 us: 1.12x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.33 ms: 1.52x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.78 ms: 1.16x slower                                  |
| Geometric mean         | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 150 us: 3.41x faster                                   |
| generators               | 76.8 ms                                                | 31.2 ms: 2.46x faster                                  |
| deltablue                | 7.42 ms                                                | 3.50 ms: 2.12x faster                                  |
| richards_super           | 90.7 ms                                                | 49.6 ms: 1.83x faster                                  |
| asyncio_tcp              | 925 ms                                                 | 514 ms: 1.80x faster                                   |
| logging_silent           | 175 ns                                                 | 100.0 ns: 1.75x faster                                 |
| richards                 | 74.9 ms                                                | 44.0 ms: 1.70x faster                                  |
| go                       | 229 ms                                                 | 135 ms: 1.70x faster                                   |
| chaos                    | 106 ms                                                 | 63.3 ms: 1.68x faster                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                 |
| scimark_sor              | 197 ms                                                 | 123 ms: 1.60x faster                                   |
| nbody                    | 142 ms                                                 | 89.9 ms: 1.58x faster                                  |
| raytrace                 | 464 ms                                                 | 297 ms: 1.56x faster                                   |
| hexiom                   | 9.53 ms                                                | 6.13 ms: 1.55x faster                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.34 ms: 1.54x faster                                  |
| scimark_monte_carlo      | 108 ms                                                 | 71.0 ms: 1.53x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.52x faster                                 |
| async_tree_none          | 717 ms                                                 | 471 ms: 1.52x faster                                   |
| crypto_pyaes             | 118 ms                                                 | 78.0 ms: 1.52x faster                                  |
| python_startup           | 14.2 ms                                                | 9.33 ms: 1.52x faster                                  |
| pyflate                  | 673 ms                                                 | 450 ms: 1.50x faster                                   |
| async_tree_memoization   | 854 ms                                                 | 576 ms: 1.48x faster                                   |
| sqlglot_transpile        | 2.45 ms                                                | 1.66 ms: 1.47x faster                                  |
| pickle_pure_python       | 455 us                                                 | 309 us: 1.47x faster                                   |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                   |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.43x faster                                  |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.43x faster                                   |
| deepcopy_memo            | 52.3 us                                                | 37.1 us: 1.41x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.39x faster                                   |
| json_dumps               | 13.5 ms                                                | 9.84 ms: 1.38x faster                                  |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                  |
| float                    | 111 ms                                                 | 80.6 ms: 1.37x faster                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 710 ms: 1.34x faster                                   |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.33x faster                                 |
| pycparser                | 1.50 sec                                               | 1.13 sec: 1.33x faster                                 |
| tomli_loads              | 2.92 sec                                               | 2.20 sec: 1.32x faster                                 |
| logging_simple           | 8.07 us                                                | 6.23 us: 1.30x faster                                  |
| pprint_safe_repr         | 955 ms                                                 | 739 ms: 1.29x faster                                   |
| comprehensions           | 26.8 us                                                | 20.8 us: 1.29x faster                                  |
| tornado_http             | 127 ms                                                 | 99.3 ms: 1.28x faster                                  |
| logging_format           | 8.91 us                                                | 6.98 us: 1.28x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 59.3 ms: 1.26x faster                                  |
| 2to3                     | 336 ms                                                 | 268 ms: 1.25x faster                                   |
| deepcopy                 | 442 us                                                 | 353 us: 1.25x faster                                   |
| mypy2                    | 428 ms                                                 | 344 ms: 1.25x faster                                   |
| unpack_sequence          | 64.7 ns                                                | 51.9 ns: 1.25x faster                                  |
| nqueens                  | 100 ms                                                 | 80.8 ms: 1.24x faster                                  |
| fannkuch                 | 486 ms                                                 | 394 ms: 1.23x faster                                   |
| sqlglot_normalize        | 135 ms                                                 | 110 ms: 1.23x faster                                   |
| deepcopy_reduce          | 3.82 us                                                | 3.13 us: 1.22x faster                                  |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                   |
| sqlglot_optimize         | 65.3 ms                                                | 54.1 ms: 1.21x faster                                  |
| scimark_fft              | 424 ms                                                 | 360 ms: 1.18x faster                                   |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.65 ms: 1.17x faster                                  |
| docutils                 | 3.17 sec                                               | 2.71 sec: 1.17x faster                                 |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                  |
| sqlalchemy_declarative   | 165 ms                                                 | 144 ms: 1.15x faster                                   |
| bench_thread_pool        | 947 us                                                 | 834 us: 1.14x faster                                   |
| regex_v8                 | 25.0 ms                                                | 22.1 ms: 1.13x faster                                  |
| json                     | 5.42 ms                                                | 4.78 ms: 1.13x faster                                  |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.8 ms: 1.13x faster                                  |
| dulwich_log              | 75.9 ms                                                | 67.9 ms: 1.12x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.0 ms: 1.11x faster                                  |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.11x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 85.2 ms: 1.11x faster                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                  |
| meteor_contest           | 115 ms                                                 | 107 ms: 1.07x faster                                   |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                   |
| regex_dna                | 222 ms                                                 | 211 ms: 1.05x faster                                   |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                  |
| pickle_list              | 4.56 us                                                | 4.61 us: 1.01x slower                                  |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                  |
| unpickle_list            | 4.82 us                                                | 4.96 us: 1.03x slower                                  |
| gc_traversal             | 3.84 ms                                                | 3.98 ms: 1.04x slower                                  |
| async_generators         | 425 ms                                                 | 448 ms: 1.05x slower                                   |
| pidigits                 | 190 ms                                                 | 200 ms: 1.06x slower                                   |
| telco                    | 6.54 ms                                                | 6.92 ms: 1.06x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.54 ms: 1.10x slower                                  |
| unpickle                 | 14.1 us                                                | 15.8 us: 1.12x slower                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.78 ms: 1.16x slower                                  |
| pickle_dict              | 27.3 us                                                | 31.9 us: 1.17x slower                                  |
| dask                     | 423 ms                                                 | 536 ms: 1.27x slower                                   |
| coverage                 | 72.8 ms                                                | 95.7 ms: 1.31x slower                                  |
| Geometric mean           | (ref)                                                  | 1.28x faster                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x
