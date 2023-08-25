
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: b0e1f9c
- commit date: 2022-11-19
- overall geometric mean: 1.32x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 245 ms: 1.37x faster                                   |
| chameleon      | 9.06 ms                                                | 6.49 ms: 1.40x faster                                  |
| html5lib       | 85.9 ms                                                | 59.1 ms: 1.45x faster                                  |
| tornado_http   | 127 ms                                                 | 92.7 ms: 1.37x faster                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 71.6 ms: 1.54x faster                                  |
| nbody          | 142 ms                                                 | 94.1 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.39x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| regex_dna      | 222 ms                                                 | 213 ms: 1.04x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.77 ms: 1.17x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                   |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.49x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.42 ms: 1.44x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 52.9 ms: 1.42x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 76.4 ms: 1.23x faster                                  |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                  |
| pickle_list          | 4.56 us                                                | 4.11 us: 1.11x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                   |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                  |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| unpickle_list        | 4.82 us                                                | 5.10 us: 1.06x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.51 ms: 1.66x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.25 ms: 1.07x slower                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 30.3 ms                                                | 20.4 ms: 1.48x faster                                  |
| mako            | 14.8 ms                                                | 9.94 ms: 1.48x faster                                  |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                  |
| genshi_xml      | 63.3 ms                                                | 46.2 ms: 1.37x faster                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.23 ms: 2.30x faster                                  |
| logging_silent          | 175 ns                                                 | 91.1 ns: 1.92x faster                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                   |
| richards                | 74.9 ms                                                | 41.6 ms: 1.80x faster                                  |
| go                      | 229 ms                                                 | 135 ms: 1.69x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 64.0 ms: 1.69x faster                                  |
| pyflate                 | 673 ms                                                 | 403 ms: 1.67x faster                                   |
| raytrace                | 464 ms                                                 | 278 ms: 1.67x faster                                   |
| python_startup          | 14.2 ms                                                | 8.51 ms: 1.66x faster                                  |
| chaos                   | 106 ms                                                 | 66.0 ms: 1.61x faster                                  |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 74.3 ms: 1.59x faster                                  |
| scimark_lu              | 163 ms                                                 | 104 ms: 1.57x faster                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.33 ms: 1.55x faster                                  |
| float                   | 111 ms                                                 | 71.6 ms: 1.54x faster                                  |
| spectral_norm           | 150 ms                                                 | 97.6 ms: 1.54x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.21 ms: 1.53x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.61 ms: 1.52x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 42.9 ns: 1.51x faster                                  |
| nbody                   | 142 ms                                                 | 94.1 ms: 1.50x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.49x faster                                   |
| genshi_text             | 30.3 ms                                                | 20.4 ms: 1.48x faster                                  |
| mako                    | 14.8 ms                                                | 9.94 ms: 1.48x faster                                  |
| html5lib                | 85.9 ms                                                | 59.1 ms: 1.45x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                 |
| json_dumps              | 13.5 ms                                                | 9.42 ms: 1.44x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 673 ms: 1.42x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 52.9 ms: 1.42x faster                                  |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                  |
| logging_format          | 8.91 us                                                | 6.35 us: 1.40x faster                                  |
| scimark_fft             | 424 ms                                                 | 303 ms: 1.40x faster                                   |
| logging_simple          | 8.07 us                                                | 5.77 us: 1.40x faster                                  |
| chameleon               | 9.06 ms                                                | 6.49 ms: 1.40x faster                                  |
| regex_compile           | 177 ms                                                 | 127 ms: 1.39x faster                                   |
| thrift                  | 1.03 ms                                                | 746 us: 1.39x faster                                   |
| aiohttp                 | 1.38 ms                                                | 999 us: 1.38x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.96 ms: 1.38x faster                                  |
| tornado_http            | 127 ms                                                 | 92.7 ms: 1.37x faster                                  |
| 2to3                    | 336 ms                                                 | 245 ms: 1.37x faster                                   |
| genshi_xml              | 63.3 ms                                                | 46.2 ms: 1.37x faster                                  |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.36x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                 |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                 |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                   |
| fannkuch                | 486 ms                                                 | 369 ms: 1.32x faster                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 729 ms: 1.31x faster                                   |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                  |
| async_tree_memoization  | 854 ms                                                 | 665 ms: 1.28x faster                                   |
| coroutines              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.98 us: 1.28x faster                                  |
| dulwich_log             | 75.9 ms                                                | 60.6 ms: 1.25x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 76.4 ms: 1.23x faster                                  |
| nqueens                 | 100 ms                                                 | 81.5 ms: 1.23x faster                                  |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                   |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                  |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                  |
| json                    | 5.42 ms                                                | 4.67 ms: 1.16x faster                                  |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.64 us: 1.11x faster                                  |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                   |
| pickle_list             | 4.56 us                                                | 4.11 us: 1.11x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.09x faster                                   |
| mdp                     | 2.82 sec                                               | 2.65 sec: 1.07x faster                                 |
| telco                   | 6.54 ms                                                | 6.27 ms: 1.04x faster                                  |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                  |
| regex_dna               | 222 ms                                                 | 213 ms: 1.04x faster                                   |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                   |
| generators              | 76.8 ms                                                | 78.0 ms: 1.02x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.10 us: 1.06x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.25 ms: 1.07x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.0 us: 1.14x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.77 ms: 1.17x slower                                  |
| coverage                | 72.8 ms                                                | 98.2 ms: 1.35x slower                                  |
| Geometric mean          | (ref)                                                  | 1.32x faster                                           |
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221119-3.12.0a3+-b0e1f9c/bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x
