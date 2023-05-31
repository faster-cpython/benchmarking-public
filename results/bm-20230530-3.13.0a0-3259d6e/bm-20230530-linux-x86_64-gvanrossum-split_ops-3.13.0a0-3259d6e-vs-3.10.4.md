
# Results vs. 3.10.4

- fork: gvanrossum
- ref: split_ops
- machine: linux-x86_64
- commit hash: 3259d6e
- commit date: 2023-05-30
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.74 sec: 1.16x faster                                         |
| tornado_http   | 127 ms                                                 | 103 ms: 1.24x faster                                           |
| Geometric mean | (ref)                                                  | 1.20x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.1 ms: 1.59x faster                                          |
| float          | 111 ms                                                 | 81.8 ms: 1.35x faster                                          |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                  | 1.27x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                           |
| regex_v8       | 25.0 ms                                                | 23.3 ms: 1.07x faster                                          |
| regex_dna      | 222 ms                                                 | 219 ms: 1.01x faster                                           |
| regex_effbot   | 3.23 ms                                                | 3.71 ms: 1.15x slower                                          |
| Geometric mean | (ref)                                                  | 1.04x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 317 us: 1.44x faster                                           |
| unpickle_pure_python | 300 us                                                 | 217 us: 1.39x faster                                           |
| json_dumps           | 13.5 ms                                                | 9.97 ms: 1.36x faster                                          |
| tomli_loads          | 2.92 sec                                               | 2.24 sec: 1.30x faster                                         |
| xml_etree_process    | 74.9 ms                                                | 59.3 ms: 1.26x faster                                          |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                          |
| xml_etree_generate   | 94.2 ms                                                | 85.1 ms: 1.11x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                           |
| pickle_list          | 4.56 us                                                | 4.49 us: 1.01x faster                                          |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                          |
| unpickle_list        | 4.82 us                                                | 4.98 us: 1.03x slower                                          |
| unpickle             | 14.1 us                                                | 15.1 us: 1.07x slower                                          |
| pickle_dict          | 27.3 us                                                | 31.7 us: 1.16x slower                                          |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.33 ms: 1.52x faster                                          |
| python_startup_no_site | 5.82 ms                                                | 6.79 ms: 1.17x slower                                          |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.49x faster                                           |
| generators               | 76.8 ms                                                | 31.5 ms: 2.44x faster                                          |
| deltablue                | 7.42 ms                                                | 3.52 ms: 2.11x faster                                          |
| asyncio_tcp              | 925 ms                                                 | 509 ms: 1.82x faster                                           |
| richards_super           | 90.7 ms                                                | 50.6 ms: 1.79x faster                                          |
| logging_silent           | 175 ns                                                 | 100 ns: 1.75x faster                                           |
| go                       | 229 ms                                                 | 136 ms: 1.69x faster                                           |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                         |
| richards                 | 74.9 ms                                                | 45.2 ms: 1.66x faster                                          |
| chaos                    | 106 ms                                                 | 64.9 ms: 1.64x faster                                          |
| scimark_sor              | 197 ms                                                 | 123 ms: 1.60x faster                                           |
| nbody                    | 142 ms                                                 | 89.1 ms: 1.59x faster                                          |
| raytrace                 | 464 ms                                                 | 300 ms: 1.55x faster                                           |
| sqlglot_parse            | 2.06 ms                                                | 1.35 ms: 1.53x faster                                          |
| hexiom                   | 9.53 ms                                                | 6.27 ms: 1.52x faster                                          |
| python_startup           | 14.2 ms                                                | 9.33 ms: 1.52x faster                                          |
| pyflate                  | 673 ms                                                 | 447 ms: 1.50x faster                                           |
| crypto_pyaes             | 118 ms                                                 | 78.8 ms: 1.50x faster                                          |
| scimark_monte_carlo      | 108 ms                                                 | 72.3 ms: 1.50x faster                                          |
| sqlglot_transpile        | 2.45 ms                                                | 1.67 ms: 1.47x faster                                          |
| async_tree_io            | 1.77 sec                                               | 1.22 sec: 1.45x faster                                         |
| async_tree_none          | 717 ms                                                 | 495 ms: 1.45x faster                                           |
| pickle_pure_python       | 455 us                                                 | 317 us: 1.44x faster                                           |
| scimark_lu               | 163 ms                                                 | 114 ms: 1.43x faster                                           |
| async_tree_memoization   | 854 ms                                                 | 599 ms: 1.43x faster                                           |
| coroutines               | 31.8 ms                                                | 22.5 ms: 1.42x faster                                          |
| deepcopy_memo            | 52.3 us                                                | 37.4 us: 1.40x faster                                          |
| spectral_norm            | 150 ms                                                 | 108 ms: 1.39x faster                                           |
| unpickle_pure_python     | 300 us                                                 | 217 us: 1.39x faster                                           |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                          |
| json_dumps               | 13.5 ms                                                | 9.97 ms: 1.36x faster                                          |
| float                    | 111 ms                                                 | 81.8 ms: 1.35x faster                                          |
| pprint_pformat           | 1.99 sec                                               | 1.52 sec: 1.31x faster                                         |
| tomli_loads              | 2.92 sec                                               | 2.24 sec: 1.30x faster                                         |
| comprehensions           | 26.8 us                                                | 20.6 us: 1.30x faster                                          |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 734 ms: 1.29x faster                                           |
| pycparser                | 1.50 sec                                               | 1.17 sec: 1.28x faster                                         |
| logging_simple           | 8.07 us                                                | 6.31 us: 1.28x faster                                          |
| pprint_safe_repr         | 955 ms                                                 | 748 ms: 1.28x faster                                           |
| logging_format           | 8.91 us                                                | 6.99 us: 1.27x faster                                          |
| xml_etree_process        | 74.9 ms                                                | 59.3 ms: 1.26x faster                                          |
| unpack_sequence          | 64.7 ns                                                | 51.8 ns: 1.25x faster                                          |
| tornado_http             | 127 ms                                                 | 103 ms: 1.24x faster                                           |
| fannkuch                 | 486 ms                                                 | 393 ms: 1.24x faster                                           |
| mypy2                    | 428 ms                                                 | 347 ms: 1.24x faster                                           |
| deepcopy                 | 442 us                                                 | 358 us: 1.23x faster                                           |
| sqlglot_normalize        | 135 ms                                                 | 111 ms: 1.22x faster                                           |
| regex_compile            | 177 ms                                                 | 146 ms: 1.21x faster                                           |
| nqueens                  | 100 ms                                                 | 83.0 ms: 1.21x faster                                          |
| scimark_fft              | 424 ms                                                 | 353 ms: 1.20x faster                                           |
| sqlglot_optimize         | 65.3 ms                                                | 54.5 ms: 1.20x faster                                          |
| deepcopy_reduce          | 3.82 us                                                | 3.22 us: 1.19x faster                                          |
| docutils                 | 3.17 sec                                               | 2.74 sec: 1.16x faster                                         |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                          |
| bench_thread_pool        | 947 us                                                 | 835 us: 1.13x faster                                           |
| json                     | 5.42 ms                                                | 4.81 ms: 1.13x faster                                          |
| dulwich_log              | 75.9 ms                                                | 68.3 ms: 1.11x faster                                          |
| xml_etree_generate       | 94.2 ms                                                | 85.1 ms: 1.11x faster                                          |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                          |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                           |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.02 ms: 1.09x faster                                          |
| regex_v8                 | 25.0 ms                                                | 23.3 ms: 1.07x faster                                          |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                           |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                          |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                          |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                           |
| gc_traversal             | 3.84 ms                                                | 3.61 ms: 1.06x faster                                          |
| mdp                      | 2.82 sec                                               | 2.71 sec: 1.04x faster                                         |
| pickle_list              | 4.56 us                                                | 4.49 us: 1.01x faster                                          |
| regex_dna                | 222 ms                                                 | 219 ms: 1.01x faster                                           |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                          |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                          |
| unpickle_list            | 4.82 us                                                | 4.98 us: 1.03x slower                                          |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                           |
| telco                    | 6.54 ms                                                | 6.90 ms: 1.06x slower                                          |
| unpickle                 | 14.1 us                                                | 15.1 us: 1.07x slower                                          |
| async_generators         | 425 ms                                                 | 456 ms: 1.07x slower                                           |
| regex_effbot             | 3.23 ms                                                | 3.71 ms: 1.15x slower                                          |
| pickle_dict              | 27.3 us                                                | 31.7 us: 1.16x slower                                          |
| python_startup_no_site   | 5.82 ms                                                | 6.79 ms: 1.17x slower                                          |
| dask                     | 423 ms                                                 | 539 ms: 1.28x slower                                           |
| coverage                 | 72.8 ms                                                | 98.2 ms: 1.35x slower                                          |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                   |
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
