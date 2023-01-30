
# Results vs. 3.10.4

- fork: python
- ref: d9dff4c8b5ab41c47af0
- machine: linux-x86_64
- commit hash: d9dff4c
- commit date: 2023-01-12
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 253 ms: 1.31x faster                                                   |
| chameleon      | 8.86 ms                                                | 6.39 ms: 1.39x faster                                                  |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                 |
| html5lib       | 85.8 ms                                                | 59.7 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.4 ms: 1.49x faster                                                  |
| nbody          | 136 ms                                                 | 94.4 ms: 1.44x faster                                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                  |
| regex_dna      | 214 ms                                                 | 206 ms: 1.04x faster                                                   |
| regex_effbot   | 3.21 ms                                                | 3.61 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 282 us: 1.61x faster                                                   |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.50x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.39 ms: 1.44x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 53.3 ms: 1.40x faster                                                  |
| xml_etree_generate   | 93.3 ms                                                | 76.2 ms: 1.22x faster                                                  |
| json_loads           | 28.9 us                                                | 23.6 us: 1.22x faster                                                  |
| pickle_list          | 4.50 us                                                | 4.04 us: 1.11x faster                                                  |
| unpickle             | 14.3 us                                                | 12.9 us: 1.10x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.04x faster                                                   |
| pickle_dict          | 28.3 us                                                | 30.4 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.58 ms: 1.62x faster                                                  |
| python_startup_no_site | 5.76 ms                                                | 6.13 ms: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                  |
| mako            | 14.3 ms                                                | 9.77 ms: 1.46x faster                                                  |
| django_template | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                  |
| genshi_xml      | 63.6 ms                                                | 47.0 ms: 1.35x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.20 ms: 2.31x faster                                                  |
| logging_silent          | 173 ns                                                 | 89.8 ns: 1.93x faster                                                  |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.82x faster                                                   |
| richards                | 71.4 ms                                                | 41.3 ms: 1.73x faster                                                  |
| pyflate                 | 675 ms                                                 | 400 ms: 1.69x faster                                                   |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                   |
| raytrace                | 461 ms                                                 | 283 ms: 1.63x faster                                                   |
| scimark_monte_carlo     | 105 ms                                                 | 64.5 ms: 1.63x faster                                                  |
| python_startup          | 13.9 ms                                                | 8.58 ms: 1.62x faster                                                  |
| pickle_pure_python      | 453 us                                                 | 282 us: 1.61x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 74.8 ms: 1.57x faster                                                  |
| hexiom                  | 9.42 ms                                                | 6.02 ms: 1.56x faster                                                  |
| chaos                   | 104 ms                                                 | 66.8 ms: 1.56x faster                                                  |
| spectral_norm           | 148 ms                                                 | 97.1 ms: 1.52x faster                                                  |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                  |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.50x faster                                                   |
| float                   | 108 ms                                                 | 72.4 ms: 1.49x faster                                                  |
| deepcopy_memo           | 50.0 us                                                | 33.8 us: 1.48x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.39 ms: 1.46x faster                                                  |
| mako                    | 14.3 ms                                                | 9.77 ms: 1.46x faster                                                  |
| scimark_lu              | 158 ms                                                 | 109 ms: 1.46x faster                                                   |
| nbody                   | 136 ms                                                 | 94.4 ms: 1.44x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.39 ms: 1.44x faster                                                  |
| html5lib                | 85.8 ms                                                | 59.7 ms: 1.44x faster                                                  |
| sqlglot_transpile       | 2.42 ms                                                | 1.69 ms: 1.43x faster                                                  |
| pprint_pformat          | 1.97 sec                                               | 1.39 sec: 1.42x faster                                                 |
| logging_simple          | 8.06 us                                                | 5.74 us: 1.40x faster                                                  |
| django_template         | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                  |
| pprint_safe_repr        | 943 ms                                                 | 673 ms: 1.40x faster                                                   |
| xml_etree_process       | 74.5 ms                                                | 53.3 ms: 1.40x faster                                                  |
| logging_format          | 8.92 us                                                | 6.42 us: 1.39x faster                                                  |
| chameleon               | 8.86 ms                                                | 6.39 ms: 1.39x faster                                                  |
| thrift                  | 1.03 ms                                                | 755 us: 1.37x faster                                                   |
| genshi_xml              | 63.6 ms                                                | 47.0 ms: 1.35x faster                                                  |
| async_tree_none         | 713 ms                                                 | 528 ms: 1.35x faster                                                   |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                 |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.11 ms: 1.33x faster                                                  |
| scimark_fft             | 414 ms                                                 | 312 ms: 1.33x faster                                                   |
| unpack_sequence         | 59.5 ns                                                | 45.1 ns: 1.32x faster                                                  |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.31x faster                                                 |
| 2to3                    | 332 ms                                                 | 253 ms: 1.31x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 657 ms: 1.30x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.3 ms: 1.30x faster                                                  |
| deepcopy                | 429 us                                                 | 331 us: 1.30x faster                                                   |
| coroutines              | 31.7 ms                                                | 24.7 ms: 1.28x faster                                                  |
| deepcopy_reduce         | 3.75 us                                                | 2.95 us: 1.27x faster                                                  |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                 |
| fannkuch                | 477 ms                                                 | 377 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 754 ms: 1.26x faster                                                   |
| mypy                    | 1.01 sec                                               | 810 ms: 1.25x faster                                                   |
| nqueens                 | 99.3 ms                                                | 80.3 ms: 1.24x faster                                                  |
| xml_etree_generate      | 93.3 ms                                                | 76.2 ms: 1.22x faster                                                  |
| json_loads              | 28.9 us                                                | 23.6 us: 1.22x faster                                                  |
| bench_thread_pool       | 943 us                                                 | 776 us: 1.21x faster                                                   |
| dulwich_log             | 75.5 ms                                                | 62.3 ms: 1.21x faster                                                  |
| async_generators        | 428 ms                                                 | 355 ms: 1.21x faster                                                   |
| sympy_integrate         | 23.9 ms                                                | 20.2 ms: 1.18x faster                                                  |
| sympy_expand            | 537 ms                                                 | 458 ms: 1.17x faster                                                   |
| sympy_str               | 324 ms                                                 | 282 ms: 1.15x faster                                                   |
| json                    | 5.35 ms                                                | 4.70 ms: 1.14x faster                                                  |
| sqlite_synth            | 2.90 us                                                | 2.57 us: 1.13x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.50 sec: 1.13x faster                                                 |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.13x faster                                                   |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                  |
| pickle_list             | 4.50 us                                                | 4.04 us: 1.11x faster                                                  |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                  |
| unpickle                | 14.3 us                                                | 12.9 us: 1.10x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.07x faster                                                   |
| telco                   | 6.68 ms                                                | 6.33 ms: 1.06x faster                                                  |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.04x faster                                                   |
| regex_dna               | 214 ms                                                 | 206 ms: 1.04x faster                                                   |
| generators              | 75.8 ms                                                | 75.4 ms: 1.00x faster                                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                   |
| python_startup_no_site  | 5.76 ms                                                | 6.13 ms: 1.06x slower                                                  |
| pickle_dict             | 28.3 us                                                | 30.4 us: 1.07x slower                                                  |
| regex_effbot            | 3.21 ms                                                | 3.61 ms: 1.12x slower                                                  |
| coverage                | 75.3 ms                                                | 101 ms: 1.34x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (3): unpickle_list, pickle, bench_mp_pool
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230112-3.12.0a4+-d9dff4c/bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
