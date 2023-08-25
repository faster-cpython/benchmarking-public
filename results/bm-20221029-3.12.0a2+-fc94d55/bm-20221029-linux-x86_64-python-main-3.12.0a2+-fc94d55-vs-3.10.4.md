
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: fc94d55
- commit date: 2022-10-29
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 248 ms: 1.35x faster                                   |
| chameleon      | 9.06 ms                                                | 6.37 ms: 1.42x faster                                  |
| html5lib       | 85.9 ms                                                | 59.5 ms: 1.44x faster                                  |
| tornado_http   | 127 ms                                                 | 93.1 ms: 1.37x faster                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 72.9 ms: 1.52x faster                                  |
| nbody          | 142 ms                                                 | 98.1 ms: 1.44x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.37x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.9 ms: 1.09x faster                                  |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.69 ms: 1.14x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.59x faster                                   |
| unpickle_pure_python | 300 us                                                 | 205 us: 1.46x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.31 ms: 1.45x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.1 ms: 1.41x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 76.1 ms: 1.24x faster                                  |
| json_loads           | 28.8 us                                                | 23.5 us: 1.23x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| pickle_list          | 4.56 us                                                | 4.16 us: 1.09x faster                                  |
| unpickle             | 14.1 us                                                | 12.9 us: 1.09x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                  |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.37 ms: 1.69x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.08 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.72 ms: 1.52x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.1 ms: 1.44x faster                                  |
| django_template | 45.9 ms                                                | 32.0 ms: 1.43x faster                                  |
| genshi_xml      | 63.3 ms                                                | 49.2 ms: 1.29x faster                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.30 ms: 2.25x faster                                  |
| logging_silent          | 175 ns                                                 | 94.4 ns: 1.86x faster                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                   |
| richards                | 74.9 ms                                                | 43.4 ms: 1.73x faster                                  |
| python_startup          | 14.2 ms                                                | 8.37 ms: 1.69x faster                                  |
| pyflate                 | 673 ms                                                 | 399 ms: 1.69x faster                                   |
| go                      | 229 ms                                                 | 137 ms: 1.67x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 65.6 ms: 1.65x faster                                  |
| raytrace                | 464 ms                                                 | 285 ms: 1.63x faster                                   |
| spectral_norm           | 150 ms                                                 | 94.1 ms: 1.59x faster                                  |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.59x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 74.7 ms: 1.58x faster                                  |
| chaos                   | 106 ms                                                 | 67.4 ms: 1.58x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.54x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.22 ms: 1.53x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.3 us: 1.53x faster                                  |
| mako                    | 14.8 ms                                                | 9.72 ms: 1.52x faster                                  |
| float                   | 111 ms                                                 | 72.9 ms: 1.52x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.63 ms: 1.50x faster                                  |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                   |
| unpickle_pure_python    | 300 us                                                 | 205 us: 1.46x faster                                   |
| json_dumps              | 13.5 ms                                                | 9.31 ms: 1.45x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                 |
| nbody                   | 142 ms                                                 | 98.1 ms: 1.44x faster                                  |
| html5lib                | 85.9 ms                                                | 59.5 ms: 1.44x faster                                  |
| genshi_text             | 30.3 ms                                                | 21.1 ms: 1.44x faster                                  |
| django_template         | 45.9 ms                                                | 32.0 ms: 1.43x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 670 ms: 1.42x faster                                   |
| chameleon               | 9.06 ms                                                | 6.37 ms: 1.42x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.1 ms: 1.41x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 46.0 ns: 1.41x faster                                  |
| thrift                  | 1.03 ms                                                | 736 us: 1.41x faster                                   |
| logging_simple          | 8.07 us                                                | 5.78 us: 1.40x faster                                  |
| logging_format          | 8.91 us                                                | 6.41 us: 1.39x faster                                  |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.37x faster                                 |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                  |
| tornado_http            | 127 ms                                                 | 93.1 ms: 1.37x faster                                  |
| regex_compile           | 177 ms                                                 | 130 ms: 1.37x faster                                   |
| 2to3                    | 336 ms                                                 | 248 ms: 1.35x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                  |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                 |
| async_tree_memoization  | 854 ms                                                 | 638 ms: 1.34x faster                                   |
| async_tree_none         | 717 ms                                                 | 536 ms: 1.34x faster                                   |
| scimark_fft             | 424 ms                                                 | 318 ms: 1.33x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.91 us: 1.31x faster                                  |
| coroutines              | 31.8 ms                                                | 24.4 ms: 1.31x faster                                  |
| fannkuch                | 486 ms                                                 | 373 ms: 1.30x faster                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 737 ms: 1.29x faster                                   |
| genshi_xml              | 63.3 ms                                                | 49.2 ms: 1.29x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.27 ms: 1.28x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                | 51.5 ms: 1.27x faster                                  |
| nqueens                 | 100 ms                                                 | 80.7 ms: 1.24x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 76.1 ms: 1.24x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.6 ms: 1.23x faster                                  |
| json_loads              | 28.8 us                                                | 23.5 us: 1.23x faster                                  |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.19x faster                                  |
| sympy_str               | 328 ms                                                 | 282 ms: 1.16x faster                                   |
| json                    | 5.42 ms                                                | 4.67 ms: 1.16x faster                                  |
| pylint                  | 525 ms                                                 | 459 ms: 1.14x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.13x faster                                  |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.13x faster                                   |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.64 us: 1.11x faster                                  |
| mdp                     | 2.82 sec                                               | 2.54 sec: 1.11x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| regex_v8                | 25.0 ms                                                | 22.9 ms: 1.09x faster                                  |
| pickle_list             | 4.56 us                                                | 4.16 us: 1.09x faster                                  |
| unpickle                | 14.1 us                                                | 12.9 us: 1.09x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| generators              | 76.8 ms                                                | 72.6 ms: 1.06x faster                                  |
| regex_dna               | 222 ms                                                 | 210 ms: 1.06x faster                                   |
| telco                   | 6.54 ms                                                | 6.31 ms: 1.04x faster                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                  |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.08 ms: 1.05x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.69 ms: 1.14x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.6 us: 1.16x slower                                  |
| coverage                | 72.8 ms                                                | 97.3 ms: 1.34x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221029-3.12.0a2+-fc94d55/bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x
