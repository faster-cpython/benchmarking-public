
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 9471106
- commit date: 2022-01-13
- overall geometric mean: 1.23x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 335 ms                                                 | 264 ms: 1.27x faster                                  |
| chameleon      | 9.17 ms                                                | 7.55 ms: 1.21x faster                                 |
| html5lib       | 85.9 ms                                                | 68.1 ms: 1.26x faster                                 |
| tornado_http   | 128 ms                                                 | 107 ms: 1.20x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.1 ms: 1.51x faster                                 |
| float          | 109 ms                                                 | 78.0 ms: 1.40x faster                                 |
| pidigits       | 190 ms                                                 | 194 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 138 ms: 1.28x faster                                  |
| regex_dna      | 214 ms                                                 | 212 ms: 1.01x faster                                  |
| regex_v8       | 25.0 ms                                                | 24.8 ms: 1.01x faster                                 |
| regex_effbot   | 3.19 ms                                                | 3.25 ms: 1.02x slower                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 329 us: 1.37x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 56.9 ms: 1.31x faster                                 |
| unpickle_pure_python | 302 us                                                 | 254 us: 1.19x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 80.2 ms: 1.17x faster                                 |
| json_loads           | 28.7 us                                                | 25.1 us: 1.14x faster                                 |
| json_dumps           | 13.4 ms                                                | 12.4 ms: 1.09x faster                                 |
| pickle_list          | 4.72 us                                                | 4.37 us: 1.08x faster                                 |
| xml_etree_parse      | 163 ms                                                 | 155 ms: 1.05x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.03x faster                                  |
| pickle_dict          | 27.6 us                                                | 26.8 us: 1.03x faster                                 |
| pickle               | 10.2 us                                                | 9.95 us: 1.02x faster                                 |
| unpickle_list        | 4.92 us                                                | 5.20 us: 1.06x slower                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.07 ms: 1.75x faster                                 |
| python_startup_no_site | 5.78 ms                                                | 5.85 ms: 1.01x slower                                 |
| Geometric mean         | (ref)                                                  | 1.31x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 46.3 ms                                                | 35.2 ms: 1.32x faster                                 |
| mako            | 14.7 ms                                                | 11.5 ms: 1.27x faster                                 |
| Geometric mean  | (ref)                                                  | 1.29x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 4.16 ms: 1.75x faster                                 |
| python_startup          | 14.1 ms                                                | 8.07 ms: 1.75x faster                                 |
| scimark_sor             | 197 ms                                                 | 124 ms: 1.58x faster                                  |
| logging_silent          | 176 ns                                                 | 113 ns: 1.55x faster                                  |
| pyflate                 | 676 ms                                                 | 444 ms: 1.52x faster                                  |
| go                      | 226 ms                                                 | 148 ms: 1.52x faster                                  |
| nbody                   | 144 ms                                                 | 95.1 ms: 1.51x faster                                 |
| spectral_norm           | 150 ms                                                 | 99.0 ms: 1.51x faster                                 |
| scimark_monte_carlo     | 109 ms                                                 | 72.7 ms: 1.49x faster                                 |
| richards                | 75.2 ms                                                | 51.5 ms: 1.46x faster                                 |
| raytrace                | 467 ms                                                 | 320 ms: 1.46x faster                                  |
| chaos                   | 106 ms                                                 | 72.7 ms: 1.45x faster                                 |
| hexiom                  | 9.43 ms                                                | 6.63 ms: 1.42x faster                                 |
| scimark_lu              | 161 ms                                                 | 114 ms: 1.41x faster                                  |
| float                   | 109 ms                                                 | 78.0 ms: 1.40x faster                                 |
| crypto_pyaes            | 117 ms                                                 | 83.8 ms: 1.39x faster                                 |
| pickle_pure_python      | 452 us                                                 | 329 us: 1.37x faster                                  |
| logging_simple          | 8.10 us                                                | 5.95 us: 1.36x faster                                 |
| logging_format          | 8.85 us                                                | 6.51 us: 1.36x faster                                 |
| unpack_sequence         | 59.4 ns                                                | 44.8 ns: 1.33x faster                                 |
| django_template         | 46.3 ms                                                | 35.2 ms: 1.32x faster                                 |
| pycparser               | 1.53 sec                                               | 1.17 sec: 1.31x faster                                |
| xml_etree_process       | 74.5 ms                                                | 56.9 ms: 1.31x faster                                 |
| regex_compile           | 177 ms                                                 | 138 ms: 1.28x faster                                  |
| scimark_fft             | 421 ms                                                 | 330 ms: 1.28x faster                                  |
| thrift                  | 1.03 ms                                                | 812 us: 1.27x faster                                  |
| 2to3                    | 335 ms                                                 | 264 ms: 1.27x faster                                  |
| mako                    | 14.7 ms                                                | 11.5 ms: 1.27x faster                                 |
| html5lib                | 85.9 ms                                                | 68.1 ms: 1.26x faster                                 |
| fannkuch                | 488 ms                                                 | 392 ms: 1.24x faster                                  |
| chameleon               | 9.17 ms                                                | 7.55 ms: 1.21x faster                                 |
| tornado_http            | 128 ms                                                 | 107 ms: 1.20x faster                                  |
| nqueens                 | 100 ms                                                 | 84.0 ms: 1.19x faster                                 |
| unpickle_pure_python    | 302 us                                                 | 254 us: 1.19x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 80.2 ms: 1.17x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.69 ms: 1.16x faster                                 |
| dulwich_log             | 75.8 ms                                                | 65.8 ms: 1.15x faster                                 |
| json_loads              | 28.7 us                                                | 25.1 us: 1.14x faster                                 |
| json                    | 5.35 ms                                                | 4.74 ms: 1.13x faster                                 |
| sympy_integrate         | 24.0 ms                                                | 21.4 ms: 1.12x faster                                 |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                  |
| json_dumps              | 13.4 ms                                                | 12.4 ms: 1.09x faster                                 |
| sympy_sum               | 183 ms                                                 | 170 ms: 1.08x faster                                  |
| pickle_list             | 4.72 us                                                | 4.37 us: 1.08x faster                                 |
| sympy_str               | 325 ms                                                 | 302 ms: 1.08x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.73 us: 1.07x faster                                 |
| sympy_expand            | 534 ms                                                 | 506 ms: 1.05x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 155 ms: 1.05x faster                                  |
| pathlib                 | 20.0 ms                                                | 19.1 ms: 1.05x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.03x faster                                  |
| pickle_dict             | 27.6 us                                                | 26.8 us: 1.03x faster                                 |
| pickle                  | 10.2 us                                                | 9.95 us: 1.02x faster                                 |
| regex_dna               | 214 ms                                                 | 212 ms: 1.01x faster                                  |
| regex_v8                | 25.0 ms                                                | 24.8 ms: 1.01x faster                                 |
| python_startup_no_site  | 5.78 ms                                                | 5.85 ms: 1.01x slower                                 |
| regex_effbot            | 3.19 ms                                                | 3.25 ms: 1.02x slower                                 |
| pidigits                | 190 ms                                                 | 194 ms: 1.02x slower                                  |
| unpickle_list           | 4.92 us                                                | 5.20 us: 1.06x slower                                 |
| Geometric mean          | (ref)                                                  | 1.23x faster                                          |

Benchmark hidden because not significant (2): telco, unpickle
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
