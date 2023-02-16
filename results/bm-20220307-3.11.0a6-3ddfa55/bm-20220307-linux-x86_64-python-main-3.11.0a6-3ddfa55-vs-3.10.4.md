
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.21x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 335 ms                                                 | 268 ms: 1.25x faster                                  |
| chameleon      | 9.17 ms                                                | 6.93 ms: 1.32x faster                                 |
| html5lib       | 85.9 ms                                                | 68.6 ms: 1.25x faster                                 |
| tornado_http   | 128 ms                                                 | 99.2 ms: 1.29x faster                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 144 ms                                                 | 97.7 ms: 1.47x faster                                 |
| float          | 109 ms                                                 | 78.7 ms: 1.38x faster                                 |
| pidigits       | 190 ms                                                 | 208 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 140 ms: 1.27x faster                                  |
| regex_v8       | 25.0 ms                                                | 23.0 ms: 1.09x faster                                 |
| regex_dna      | 214 ms                                                 | 221 ms: 1.03x slower                                  |
| regex_effbot   | 3.19 ms                                                | 3.49 ms: 1.09x slower                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 335 us: 1.35x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 56.0 ms: 1.33x faster                                 |
| unpickle_pure_python | 302 us                                                 | 246 us: 1.23x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 79.6 ms: 1.18x faster                                 |
| json_dumps           | 13.4 ms                                                | 12.6 ms: 1.07x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                  |
| pickle               | 10.2 us                                                | 9.69 us: 1.05x faster                                 |
| pickle_list          | 4.72 us                                                | 4.51 us: 1.05x faster                                 |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.04x faster                                  |
| json_loads           | 28.7 us                                                | 28.1 us: 1.02x faster                                 |
| pickle_dict          | 27.6 us                                                | 28.1 us: 1.02x slower                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                          |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.20 ms: 1.72x faster                                 |
| python_startup_no_site | 5.78 ms                                                | 6.07 ms: 1.05x slower                                 |
| Geometric mean         | (ref)                                                  | 1.28x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.6 ms: 1.38x faster                                 |
| django_template | 46.3 ms                                                | 36.0 ms: 1.29x faster                                 |
| Geometric mean  | (ref)                                                  | 1.33x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 4.16 ms: 1.75x faster                                 |
| python_startup          | 14.1 ms                                                | 8.20 ms: 1.72x faster                                 |
| scimark_sor             | 197 ms                                                 | 123 ms: 1.59x faster                                  |
| logging_silent          | 176 ns                                                 | 113 ns: 1.57x faster                                  |
| richards                | 75.2 ms                                                | 48.5 ms: 1.55x faster                                 |
| go                      | 226 ms                                                 | 148 ms: 1.53x faster                                  |
| pyflate                 | 676 ms                                                 | 453 ms: 1.49x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 72.9 ms: 1.49x faster                                 |
| nbody                   | 144 ms                                                 | 97.7 ms: 1.47x faster                                 |
| raytrace                | 467 ms                                                 | 318 ms: 1.47x faster                                  |
| logging_simple          | 8.10 us                                                | 5.52 us: 1.47x faster                                 |
| logging_format          | 8.85 us                                                | 6.08 us: 1.46x faster                                 |
| chaos                   | 106 ms                                                 | 73.5 ms: 1.44x faster                                 |
| scimark_lu              | 161 ms                                                 | 115 ms: 1.39x faster                                  |
| spectral_norm           | 150 ms                                                 | 107 ms: 1.39x faster                                  |
| float                   | 109 ms                                                 | 78.7 ms: 1.38x faster                                 |
| mako                    | 14.7 ms                                                | 10.6 ms: 1.38x faster                                 |
| crypto_pyaes            | 117 ms                                                 | 84.6 ms: 1.38x faster                                 |
| pickle_pure_python      | 452 us                                                 | 335 us: 1.35x faster                                  |
| hexiom                  | 9.43 ms                                                | 7.04 ms: 1.34x faster                                 |
| xml_etree_process       | 74.5 ms                                                | 56.0 ms: 1.33x faster                                 |
| chameleon               | 9.17 ms                                                | 6.93 ms: 1.32x faster                                 |
| thrift                  | 1.03 ms                                                | 789 us: 1.31x faster                                  |
| tornado_http            | 128 ms                                                 | 99.2 ms: 1.29x faster                                 |
| django_template         | 46.3 ms                                                | 36.0 ms: 1.29x faster                                 |
| regex_compile           | 177 ms                                                 | 140 ms: 1.27x faster                                  |
| pycparser               | 1.53 sec                                               | 1.21 sec: 1.26x faster                                |
| html5lib                | 85.9 ms                                                | 68.6 ms: 1.25x faster                                 |
| 2to3                    | 335 ms                                                 | 268 ms: 1.25x faster                                  |
| scimark_fft             | 421 ms                                                 | 336 ms: 1.25x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 246 us: 1.23x faster                                  |
| fannkuch                | 488 ms                                                 | 398 ms: 1.22x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 79.6 ms: 1.18x faster                                 |
| sqlite_synth            | 2.92 us                                                | 2.51 us: 1.17x faster                                 |
| sympy_integrate         | 24.0 ms                                                | 20.9 ms: 1.15x faster                                 |
| nqueens                 | 100 ms                                                 | 87.0 ms: 1.15x faster                                 |
| dulwich_log             | 75.8 ms                                                | 66.5 ms: 1.14x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.82 ms: 1.13x faster                                 |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.12x faster                                  |
| sympy_str               | 325 ms                                                 | 289 ms: 1.12x faster                                  |
| sympy_expand            | 534 ms                                                 | 481 ms: 1.11x faster                                  |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                 |
| regex_v8                | 25.0 ms                                                | 23.0 ms: 1.09x faster                                 |
| meteor_contest          | 114 ms                                                 | 106 ms: 1.08x faster                                  |
| json                    | 5.35 ms                                                | 5.00 ms: 1.07x faster                                 |
| json_dumps              | 13.4 ms                                                | 12.6 ms: 1.07x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                  |
| pickle                  | 10.2 us                                                | 9.69 us: 1.05x faster                                 |
| pickle_list             | 4.72 us                                                | 4.51 us: 1.05x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.04x faster                                  |
| json_loads              | 28.7 us                                                | 28.1 us: 1.02x faster                                 |
| pickle_dict             | 27.6 us                                                | 28.1 us: 1.02x slower                                 |
| telco                   | 6.73 ms                                                | 6.92 ms: 1.03x slower                                 |
| regex_dna               | 214 ms                                                 | 221 ms: 1.03x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.07 ms: 1.05x slower                                 |
| regex_effbot            | 3.19 ms                                                | 3.49 ms: 1.09x slower                                 |
| pidigits                | 190 ms                                                 | 208 ms: 1.10x slower                                  |
| unpack_sequence         | 59.4 ns                                                | 131 ns: 2.20x slower                                  |
| Geometric mean          | (ref)                                                  | 1.21x faster                                          |

Benchmark hidden because not significant (2): unpickle_list, unpickle
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
