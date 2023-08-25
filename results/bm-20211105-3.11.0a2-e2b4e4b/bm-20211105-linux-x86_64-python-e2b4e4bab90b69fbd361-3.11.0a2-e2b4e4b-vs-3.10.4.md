
# Results vs. 3.10.4

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: linux-x86_64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.16x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 274 ms: 1.23x faster                                                  |
| chameleon      | 9.06 ms                                                | 7.46 ms: 1.22x faster                                                 |
| docutils       | 3.17 sec                                               | 2.79 sec: 1.13x faster                                                |
| html5lib       | 85.9 ms                                                | 71.5 ms: 1.20x faster                                                 |
| tornado_http   | 127 ms                                                 | 111 ms: 1.15x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 111 ms                                                 | 83.3 ms: 1.33x faster                                                 |
| nbody          | 142 ms                                                 | 112 ms: 1.26x faster                                                  |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                                  |
| regex_v8       | 25.0 ms                                                | 23.7 ms: 1.06x faster                                                 |
| regex_dna      | 222 ms                                                 | 219 ms: 1.01x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.26 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 74.9 ms                                                | 59.6 ms: 1.26x faster                                                 |
| pickle_pure_python   | 455 us                                                 | 364 us: 1.25x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 81.6 ms: 1.15x faster                                                 |
| json_loads           | 28.8 us                                                | 25.9 us: 1.11x faster                                                 |
| unpickle_pure_python | 300 us                                                 | 271 us: 1.11x faster                                                  |
| json_dumps           | 13.5 ms                                                | 12.4 ms: 1.09x faster                                                 |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.03x faster                                                  |
| unpickle             | 14.1 us                                                | 13.7 us: 1.03x faster                                                 |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 110 ms: 1.01x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.68 us: 1.03x slower                                                 |
| pickle_dict          | 27.3 us                                                | 28.6 us: 1.05x slower                                                 |
| unpickle_list        | 4.82 us                                                | 5.13 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 5.82 ms                                                | 5.77 ms: 1.01x faster                                                 |
| python_startup         | 14.2 ms                                                | 14.6 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 30.3 ms                                                | 24.6 ms: 1.23x faster                                                 |
| mako            | 14.8 ms                                                | 12.1 ms: 1.22x faster                                                 |
| django_template | 45.9 ms                                                | 37.9 ms: 1.21x faster                                                 |
| genshi_xml      | 63.3 ms                                                | 56.1 ms: 1.13x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 4.86 ms: 1.53x faster                                                 |
| logging_silent          | 175 ns                                                 | 117 ns: 1.50x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 43.6 ns: 1.49x faster                                                 |
| raytrace                | 464 ms                                                 | 326 ms: 1.42x faster                                                  |
| spectral_norm           | 150 ms                                                 | 106 ms: 1.42x faster                                                  |
| async_tree_none         | 717 ms                                                 | 518 ms: 1.38x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 78.4 ms: 1.38x faster                                                 |
| chaos                   | 106 ms                                                 | 77.1 ms: 1.38x faster                                                 |
| go                      | 229 ms                                                 | 167 ms: 1.37x faster                                                  |
| richards                | 74.9 ms                                                | 55.7 ms: 1.34x faster                                                 |
| generators              | 76.8 ms                                                | 57.4 ms: 1.34x faster                                                 |
| logging_simple          | 8.07 us                                                | 6.07 us: 1.33x faster                                                 |
| logging_format          | 8.91 us                                                | 6.71 us: 1.33x faster                                                 |
| float                   | 111 ms                                                 | 83.3 ms: 1.33x faster                                                 |
| crypto_pyaes            | 118 ms                                                 | 90.2 ms: 1.31x faster                                                 |
| deepcopy_memo           | 52.3 us                                                | 40.4 us: 1.29x faster                                                 |
| hexiom                  | 9.53 ms                                                | 7.42 ms: 1.28x faster                                                 |
| gunicorn                | 1.46 ms                                                | 1.15 ms: 1.27x faster                                                 |
| async_tree_memoization  | 854 ms                                                 | 676 ms: 1.26x faster                                                  |
| nbody                   | 142 ms                                                 | 112 ms: 1.26x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.41 sec: 1.26x faster                                                |
| scimark_sor             | 197 ms                                                 | 156 ms: 1.26x faster                                                  |
| thrift                  | 1.03 ms                                                | 821 us: 1.26x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 59.6 ms: 1.26x faster                                                 |
| pprint_pformat          | 1.99 sec                                               | 1.58 sec: 1.26x faster                                                |
| pprint_safe_repr        | 955 ms                                                 | 763 ms: 1.25x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 364 us: 1.25x faster                                                  |
| pyflate                 | 673 ms                                                 | 541 ms: 1.25x faster                                                  |
| genshi_text             | 30.3 ms                                                | 24.6 ms: 1.23x faster                                                 |
| 2to3                    | 336 ms                                                 | 274 ms: 1.23x faster                                                  |
| regex_compile           | 177 ms                                                 | 145 ms: 1.22x faster                                                  |
| mako                    | 14.8 ms                                                | 12.1 ms: 1.22x faster                                                 |
| chameleon               | 9.06 ms                                                | 7.46 ms: 1.22x faster                                                 |
| django_template         | 45.9 ms                                                | 37.9 ms: 1.21x faster                                                 |
| html5lib                | 85.9 ms                                                | 71.5 ms: 1.20x faster                                                 |
| scimark_lu              | 163 ms                                                 | 136 ms: 1.20x faster                                                  |
| pycparser               | 1.50 sec                                               | 1.26 sec: 1.19x faster                                                |
| scimark_fft             | 424 ms                                                 | 355 ms: 1.19x faster                                                  |
| async_generators        | 425 ms                                                 | 361 ms: 1.18x faster                                                  |
| deepcopy_reduce         | 3.82 us                                                | 3.27 us: 1.17x faster                                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 818 ms: 1.16x faster                                                  |
| deepcopy                | 442 us                                                 | 382 us: 1.16x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 81.6 ms: 1.15x faster                                                 |
| tornado_http            | 127 ms                                                 | 111 ms: 1.15x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 145 ms: 1.14x faster                                                  |
| fannkuch                | 486 ms                                                 | 427 ms: 1.14x faster                                                  |
| docutils                | 3.17 sec                                               | 2.79 sec: 1.13x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 119 ms: 1.13x faster                                                  |
| genshi_xml              | 63.3 ms                                                | 56.1 ms: 1.13x faster                                                 |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.8 ms: 1.13x faster                                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.86 ms: 1.12x faster                                                 |
| sqlglot_optimize        | 65.3 ms                                                | 58.4 ms: 1.12x faster                                                 |
| pylint                  | 525 ms                                                 | 469 ms: 1.12x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 68.3 ms: 1.11x faster                                                 |
| json_loads              | 28.8 us                                                | 25.9 us: 1.11x faster                                                 |
| flaskblogging           | 8.27 ms                                                | 7.46 ms: 1.11x faster                                                 |
| unpickle_pure_python    | 300 us                                                 | 271 us: 1.11x faster                                                  |
| coroutines              | 31.8 ms                                                | 28.8 ms: 1.11x faster                                                 |
| json                    | 5.42 ms                                                | 4.91 ms: 1.10x faster                                                 |
| nqueens                 | 100 ms                                                 | 91.4 ms: 1.09x faster                                                 |
| json_dumps              | 13.5 ms                                                | 12.4 ms: 1.09x faster                                                 |
| sympy_integrate         | 24.3 ms                                                | 22.2 ms: 1.09x faster                                                 |
| sympy_sum               | 185 ms                                                 | 170 ms: 1.08x faster                                                  |
| sympy_expand            | 545 ms                                                 | 505 ms: 1.08x faster                                                  |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.08x faster                                                  |
| sympy_str               | 328 ms                                                 | 306 ms: 1.07x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.76 us: 1.06x faster                                                 |
| bench_thread_pool       | 947 us                                                 | 892 us: 1.06x faster                                                  |
| regex_v8                | 25.0 ms                                                | 23.7 ms: 1.06x faster                                                 |
| pathlib                 | 20.0 ms                                                | 19.1 ms: 1.05x faster                                                 |
| mdp                     | 2.82 sec                                               | 2.71 sec: 1.04x faster                                                |
| xml_etree_parse         | 163 ms                                                 | 158 ms: 1.03x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 2.37 ms: 1.03x faster                                                 |
| unpickle                | 14.1 us                                                | 13.7 us: 1.03x faster                                                 |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                 |
| regex_dna               | 222 ms                                                 | 219 ms: 1.01x faster                                                  |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 110 ms: 1.01x faster                                                  |
| python_startup_no_site  | 5.82 ms                                                | 5.77 ms: 1.01x faster                                                 |
| telco                   | 6.54 ms                                                | 6.50 ms: 1.01x faster                                                 |
| regex_effbot            | 3.23 ms                                                | 3.26 ms: 1.01x slower                                                 |
| pickle_list             | 4.56 us                                                | 4.68 us: 1.03x slower                                                 |
| python_startup          | 14.2 ms                                                | 14.6 ms: 1.03x slower                                                 |
| coverage                | 72.8 ms                                                | 75.8 ms: 1.04x slower                                                 |
| pickle_dict             | 27.3 us                                                | 28.6 us: 1.05x slower                                                 |
| unpickle_list           | 4.82 us                                                | 5.13 us: 1.06x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.16x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, sqlglot_parse
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, gc_traversal, mypy2, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.13x
