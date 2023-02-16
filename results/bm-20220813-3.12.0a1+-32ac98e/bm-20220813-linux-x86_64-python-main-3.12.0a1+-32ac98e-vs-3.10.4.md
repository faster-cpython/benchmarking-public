
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 32ac98e
- commit date: 2022-08-13
- overall geometric mean: 1.33x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                   |
| chameleon      | 9.17 ms                                                | 6.30 ms: 1.46x faster                                  |
| html5lib       | 85.9 ms                                                | 62.9 ms: 1.37x faster                                  |
| tornado_http   | 128 ms                                                 | 91.6 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 91.3 ms: 1.58x faster                                  |
| float          | 109 ms                                                 | 72.6 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.40x faster                                   |
| regex_v8       | 25.0 ms                                                | 20.9 ms: 1.20x faster                                  |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.42 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                   |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                   |
| xml_etree_process    | 74.5 ms                                                | 51.3 ms: 1.45x faster                                  |
| json_dumps           | 13.4 ms                                                | 9.67 ms: 1.39x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 74.3 ms: 1.26x faster                                  |
| json_loads           | 28.7 us                                                | 24.2 us: 1.19x faster                                  |
| pickle_list          | 4.72 us                                                | 4.25 us: 1.11x faster                                  |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 155 ms: 1.05x faster                                   |
| pickle               | 10.2 us                                                | 10.5 us: 1.03x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.4 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.17 ms: 1.72x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.04 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.21 ms: 1.59x faster                                  |
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                  |
| Geometric mean  | (ref)                                                  | 1.51x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.27x faster                                  |
| logging_silent          | 176 ns                                                 | 89.6 ns: 1.97x faster                                  |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.77x faster                                   |
| python_startup          | 14.1 ms                                                | 8.17 ms: 1.72x faster                                  |
| pyflate                 | 676 ms                                                 | 397 ms: 1.70x faster                                   |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 64.7 ms: 1.68x faster                                  |
| richards                | 75.2 ms                                                | 45.1 ms: 1.67x faster                                  |
| raytrace                | 467 ms                                                 | 293 ms: 1.59x faster                                   |
| mako                    | 14.7 ms                                                | 9.21 ms: 1.59x faster                                  |
| chaos                   | 106 ms                                                 | 66.8 ms: 1.58x faster                                  |
| hexiom                  | 9.43 ms                                                | 5.97 ms: 1.58x faster                                  |
| nbody                   | 144 ms                                                 | 91.3 ms: 1.58x faster                                  |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                   |
| spectral_norm           | 150 ms                                                 | 95.1 ms: 1.57x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 74.2 ms: 1.57x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                   |
| float                   | 109 ms                                                 | 72.6 ms: 1.50x faster                                  |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                   |
| pycparser               | 1.53 sec                                               | 1.05 sec: 1.46x faster                                 |
| chameleon               | 9.17 ms                                                | 6.30 ms: 1.46x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 51.3 ms: 1.45x faster                                  |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                  |
| thrift                  | 1.03 ms                                                | 728 us: 1.42x faster                                   |
| tornado_http            | 128 ms                                                 | 91.6 ms: 1.40x faster                                  |
| regex_compile           | 177 ms                                                 | 127 ms: 1.40x faster                                   |
| logging_simple          | 8.10 us                                                | 5.81 us: 1.39x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.67 ms: 1.39x faster                                  |
| logging_format          | 8.85 us                                                | 6.39 us: 1.39x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 43.0 ns: 1.38x faster                                  |
| html5lib                | 85.9 ms                                                | 62.9 ms: 1.37x faster                                  |
| scimark_fft             | 421 ms                                                 | 308 ms: 1.37x faster                                   |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.15 ms: 1.31x faster                                  |
| fannkuch                | 488 ms                                                 | 375 ms: 1.30x faster                                   |
| xml_etree_generate      | 93.8 ms                                                | 74.3 ms: 1.26x faster                                  |
| nqueens                 | 100 ms                                                 | 80.9 ms: 1.24x faster                                  |
| dulwich_log             | 75.8 ms                                                | 61.6 ms: 1.23x faster                                  |
| regex_v8                | 25.0 ms                                                | 20.9 ms: 1.20x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.1 ms: 1.20x faster                                  |
| json_loads              | 28.7 us                                                | 24.2 us: 1.19x faster                                  |
| sympy_str               | 325 ms                                                 | 278 ms: 1.17x faster                                   |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                   |
| sympy_sum               | 183 ms                                                 | 159 ms: 1.15x faster                                   |
| json                    | 5.35 ms                                                | 4.68 ms: 1.14x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                  |
| meteor_contest          | 114 ms                                                 | 101 ms: 1.13x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                  |
| pickle_list             | 4.72 us                                                | 4.25 us: 1.11x faster                                  |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 155 ms: 1.05x faster                                   |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                   |
| telco                   | 6.73 ms                                                | 6.47 ms: 1.04x faster                                  |
| pickle                  | 10.2 us                                                | 10.5 us: 1.03x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.04 ms: 1.05x slower                                  |
| pidigits                | 190 ms                                                 | 201 ms: 1.06x slower                                   |
| regex_effbot            | 3.19 ms                                                | 3.42 ms: 1.07x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.4 us: 1.14x slower                                  |
| Geometric mean          | (ref)                                                  | 1.33x faster                                           |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
