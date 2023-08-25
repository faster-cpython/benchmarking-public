
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8baef8a
- commit date: 2022-10-02
- overall geometric mean: 1.33x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 246 ms: 1.37x faster                                   |
| chameleon      | 9.06 ms                                                | 6.38 ms: 1.42x faster                                  |
| html5lib       | 85.9 ms                                                | 59.3 ms: 1.45x faster                                  |
| tornado_http   | 127 ms                                                 | 92.8 ms: 1.37x faster                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 72.0 ms: 1.54x faster                                  |
| nbody          | 142 ms                                                 | 96.2 ms: 1.47x faster                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.40x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.17x faster                                  |
| regex_dna      | 222 ms                                                 | 204 ms: 1.08x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.32 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                   |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.49x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 52.9 ms: 1.42x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.56 ms: 1.42x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 75.3 ms: 1.25x faster                                  |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                  |
| pickle_list          | 4.56 us                                                | 4.06 us: 1.12x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                   |
| unpickle             | 14.1 us                                                | 13.5 us: 1.05x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 157 ms: 1.04x faster                                   |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.9 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.35 ms: 1.70x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.05 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.35 ms: 1.58x faster                                  |
| genshi_text     | 30.3 ms                                                | 20.7 ms: 1.46x faster                                  |
| django_template | 45.9 ms                                                | 32.4 ms: 1.42x faster                                  |
| genshi_xml      | 63.3 ms                                                | 48.4 ms: 1.31x faster                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.26 ms: 2.28x faster                                  |
| logging_silent          | 175 ns                                                 | 92.6 ns: 1.89x faster                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                   |
| go                      | 229 ms                                                 | 132 ms: 1.74x faster                                   |
| python_startup          | 14.2 ms                                                | 8.35 ms: 1.70x faster                                  |
| richards                | 74.9 ms                                                | 44.2 ms: 1.69x faster                                  |
| pyflate                 | 673 ms                                                 | 400 ms: 1.68x faster                                   |
| raytrace                | 464 ms                                                 | 278 ms: 1.67x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 65.6 ms: 1.65x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 72.8 ms: 1.63x faster                                  |
| spectral_norm           | 150 ms                                                 | 92.3 ms: 1.62x faster                                  |
| chaos                   | 106 ms                                                 | 66.4 ms: 1.60x faster                                  |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                   |
| hexiom                  | 9.53 ms                                                | 6.00 ms: 1.59x faster                                  |
| mako                    | 14.8 ms                                                | 9.35 ms: 1.58x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 33.6 us: 1.56x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.32 ms: 1.55x faster                                  |
| float                   | 111 ms                                                 | 72.0 ms: 1.54x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.61 ms: 1.52x faster                                  |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                   |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.49x faster                                   |
| unpack_sequence         | 64.7 ns                                                | 43.5 ns: 1.49x faster                                  |
| nbody                   | 142 ms                                                 | 96.2 ms: 1.47x faster                                  |
| genshi_text             | 30.3 ms                                                | 20.7 ms: 1.46x faster                                  |
| html5lib                | 85.9 ms                                                | 59.3 ms: 1.45x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                 |
| pprint_safe_repr        | 955 ms                                                 | 670 ms: 1.43x faster                                   |
| chameleon               | 9.06 ms                                                | 6.38 ms: 1.42x faster                                  |
| django_template         | 45.9 ms                                                | 32.4 ms: 1.42x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 52.9 ms: 1.42x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.56 ms: 1.42x faster                                  |
| logging_simple          | 8.07 us                                                | 5.75 us: 1.40x faster                                  |
| async_tree_none         | 717 ms                                                 | 512 ms: 1.40x faster                                   |
| regex_compile           | 177 ms                                                 | 127 ms: 1.40x faster                                   |
| logging_format          | 8.91 us                                                | 6.39 us: 1.39x faster                                  |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                   |
| tornado_http            | 127 ms                                                 | 92.8 ms: 1.37x faster                                  |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                  |
| 2to3                    | 336 ms                                                 | 246 ms: 1.37x faster                                   |
| deepcopy                | 442 us                                                 | 324 us: 1.36x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                 |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.36x faster                                 |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                  |
| scimark_fft             | 424 ms                                                 | 317 ms: 1.34x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 640 ms: 1.34x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.86 us: 1.33x faster                                  |
| coroutines              | 31.8 ms                                                | 23.9 ms: 1.33x faster                                  |
| fannkuch                | 486 ms                                                 | 371 ms: 1.31x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.17 ms: 1.31x faster                                  |
| genshi_xml              | 63.3 ms                                                | 48.4 ms: 1.31x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.31x faster                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 730 ms: 1.30x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                  |
| nqueens                 | 100 ms                                                 | 79.3 ms: 1.26x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 75.3 ms: 1.25x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.3 ms: 1.24x faster                                  |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                  |
| sympy_expand            | 545 ms                                                 | 453 ms: 1.20x faster                                   |
| json                    | 5.42 ms                                                | 4.51 ms: 1.20x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.19x faster                                  |
| pylint                  | 525 ms                                                 | 447 ms: 1.17x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.17x faster                                  |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                   |
| mdp                     | 2.82 sec                                               | 2.45 sec: 1.15x faster                                 |
| sqlite_synth            | 2.93 us                                                | 2.57 us: 1.14x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                  |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                   |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.12x faster                                   |
| pickle_list             | 4.56 us                                                | 4.06 us: 1.12x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.09x faster                                   |
| regex_dna               | 222 ms                                                 | 204 ms: 1.08x faster                                   |
| generators              | 76.8 ms                                                | 72.1 ms: 1.06x faster                                  |
| unpickle                | 14.1 us                                                | 13.5 us: 1.05x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 157 ms: 1.04x faster                                   |
| telco                   | 6.54 ms                                                | 6.33 ms: 1.03x faster                                  |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                  |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                   |
| regex_effbot            | 3.23 ms                                                | 3.32 ms: 1.03x slower                                  |
| unpickle_list           | 4.82 us                                                | 4.96 us: 1.03x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.05 ms: 1.04x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.9 us: 1.13x slower                                  |
| coverage                | 72.8 ms                                                | 96.6 ms: 1.33x slower                                  |
| Geometric mean          | (ref)                                                  | 1.33x faster                                           |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221002-3.12.0a1+-8baef8a/bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x
