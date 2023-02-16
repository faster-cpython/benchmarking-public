
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 38612a0
- commit date: 2022-06-26
- overall geometric mean: 1.33x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.17 ms                                                | 6.45 ms: 1.42x faster                                  |
| html5lib       | 85.9 ms                                                | 62.0 ms: 1.38x faster                                  |
| tornado_http   | 128 ms                                                 | 92.1 ms: 1.39x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 109 ms                                                 | 71.1 ms: 1.53x faster                                  |
| nbody          | 144 ms                                                 | 94.8 ms: 1.52x faster                                  |
| pidigits       | 190 ms                                                 | 194 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.18x faster                                  |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.61 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 294 us: 1.54x faster                                   |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                   |
| xml_etree_process    | 74.5 ms                                                | 52.0 ms: 1.43x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 75.0 ms: 1.25x faster                                  |
| json_loads           | 28.7 us                                                | 24.5 us: 1.17x faster                                  |
| pickle_list          | 4.72 us                                                | 4.15 us: 1.14x faster                                  |
| json_dumps           | 13.4 ms                                                | 12.0 ms: 1.12x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| unpickle             | 14.2 us                                                | 13.4 us: 1.06x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 155 ms: 1.05x faster                                   |
| pickle_dict          | 27.6 us                                                | 30.1 us: 1.09x slower                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.26 ms: 1.71x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.10 ms: 1.06x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.46 ms: 1.55x faster                                  |
| django_template | 46.3 ms                                                | 31.6 ms: 1.47x faster                                  |
| Geometric mean  | (ref)                                                  | 1.51x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220626-linux-x86_64-python-main-3.12.0a1+-38612a0 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.24 ms: 2.25x faster                                  |
| logging_silent          | 176 ns                                                 | 89.6 ns: 1.97x faster                                  |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.79x faster                                   |
| go                      | 226 ms                                                 | 128 ms: 1.76x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 62.4 ms: 1.74x faster                                  |
| python_startup          | 14.1 ms                                                | 8.26 ms: 1.71x faster                                  |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                   |
| raytrace                | 467 ms                                                 | 279 ms: 1.67x faster                                   |
| richards                | 75.2 ms                                                | 45.4 ms: 1.65x faster                                  |
| chaos                   | 106 ms                                                 | 63.8 ms: 1.65x faster                                  |
| spectral_norm           | 150 ms                                                 | 92.8 ms: 1.61x faster                                  |
| hexiom                  | 9.43 ms                                                | 5.94 ms: 1.59x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 73.7 ms: 1.58x faster                                  |
| scimark_lu              | 161 ms                                                 | 104 ms: 1.55x faster                                   |
| mako                    | 14.7 ms                                                | 9.46 ms: 1.55x faster                                  |
| pickle_pure_python      | 452 us                                                 | 294 us: 1.54x faster                                   |
| float                   | 109 ms                                                 | 71.1 ms: 1.53x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                   |
| nbody                   | 144 ms                                                 | 94.8 ms: 1.52x faster                                  |
| django_template         | 46.3 ms                                                | 31.6 ms: 1.47x faster                                  |
| pycparser               | 1.53 sec                                               | 1.05 sec: 1.46x faster                                 |
| xml_etree_process       | 74.5 ms                                                | 52.0 ms: 1.43x faster                                  |
| chameleon               | 9.17 ms                                                | 6.45 ms: 1.42x faster                                  |
| logging_simple          | 8.10 us                                                | 5.77 us: 1.40x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.89 ms: 1.40x faster                                  |
| tornado_http            | 128 ms                                                 | 92.1 ms: 1.39x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 42.8 ns: 1.39x faster                                  |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                   |
| logging_format          | 8.85 us                                                | 6.40 us: 1.38x faster                                  |
| html5lib                | 85.9 ms                                                | 62.0 ms: 1.38x faster                                  |
| scimark_fft             | 421 ms                                                 | 304 ms: 1.38x faster                                   |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| 2to3                    | 335 ms                                                 | 249 ms: 1.35x faster                                   |
| fannkuch                | 488 ms                                                 | 376 ms: 1.30x faster                                   |
| xml_etree_generate      | 93.8 ms                                                | 75.0 ms: 1.25x faster                                  |
| dulwich_log             | 75.8 ms                                                | 61.7 ms: 1.23x faster                                  |
| nqueens                 | 100 ms                                                 | 82.2 ms: 1.22x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.2 ms: 1.19x faster                                  |
| sympy_expand            | 534 ms                                                 | 451 ms: 1.18x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.18x faster                                  |
| sympy_str               | 325 ms                                                 | 277 ms: 1.17x faster                                   |
| json_loads              | 28.7 us                                                | 24.5 us: 1.17x faster                                  |
| sympy_sum               | 183 ms                                                 | 159 ms: 1.15x faster                                   |
| sqlite_synth            | 2.92 us                                                | 2.57 us: 1.14x faster                                  |
| pickle_list             | 4.72 us                                                | 4.15 us: 1.14x faster                                  |
| json                    | 5.35 ms                                                | 4.72 ms: 1.13x faster                                  |
| json_dumps              | 13.4 ms                                                | 12.0 ms: 1.12x faster                                  |
| meteor_contest          | 114 ms                                                 | 102 ms: 1.12x faster                                   |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.10x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| unpickle                | 14.2 us                                                | 13.4 us: 1.06x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 155 ms: 1.05x faster                                   |
| telco                   | 6.73 ms                                                | 6.44 ms: 1.05x faster                                  |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                   |
| pidigits                | 190 ms                                                 | 194 ms: 1.02x slower                                   |
| python_startup_no_site  | 5.78 ms                                                | 6.10 ms: 1.06x slower                                  |
| pickle_dict             | 27.6 us                                                | 30.1 us: 1.09x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.61 ms: 1.13x slower                                  |
| Geometric mean          | (ref)                                                  | 1.33x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, pickle
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
