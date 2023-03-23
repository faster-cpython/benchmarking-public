
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c4e4b91
- commit date: 2022-02-03
- overall geometric mean: 1.23x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 335 ms                                                 | 267 ms: 1.26x faster                                  |
| chameleon      | 9.17 ms                                                | 6.95 ms: 1.32x faster                                 |
| html5lib       | 85.9 ms                                                | 67.9 ms: 1.26x faster                                 |
| tornado_http   | 128 ms                                                 | 106 ms: 1.21x faster                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.7 ms: 1.52x faster                                 |
| float          | 109 ms                                                 | 77.5 ms: 1.40x faster                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 140 ms: 1.26x faster                                  |
| regex_v8       | 25.0 ms                                                | 24.0 ms: 1.04x faster                                 |
| regex_effbot   | 3.19 ms                                                | 3.14 ms: 1.02x faster                                 |
| regex_dna      | 214 ms                                                 | 213 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 334 us: 1.35x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 57.0 ms: 1.31x faster                                 |
| unpickle_pure_python | 302 us                                                 | 249 us: 1.21x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 79.6 ms: 1.18x faster                                 |
| json_dumps           | 13.4 ms                                                | 12.2 ms: 1.10x faster                                 |
| json_loads           | 28.7 us                                                | 26.7 us: 1.07x faster                                 |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                  |
| pickle_list          | 4.72 us                                                | 4.47 us: 1.06x faster                                 |
| unpickle             | 14.2 us                                                | 13.4 us: 1.05x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.04x faster                                  |
| pickle               | 10.2 us                                                | 9.93 us: 1.02x faster                                 |
| pickle_dict          | 27.6 us                                                | 28.1 us: 1.02x slower                                 |
| unpickle_list        | 4.92 us                                                | 5.26 us: 1.07x slower                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.13 ms: 1.73x faster                                 |
| python_startup_no_site | 5.78 ms                                                | 5.92 ms: 1.02x slower                                 |
| Geometric mean         | (ref)                                                  | 1.30x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.5 ms: 1.40x faster                                 |
| django_template | 46.3 ms                                                | 35.4 ms: 1.31x faster                                 |
| Geometric mean  | (ref)                                                  | 1.35x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 4.13 ms: 1.76x faster                                 |
| python_startup          | 14.1 ms                                                | 8.13 ms: 1.73x faster                                 |
| logging_silent          | 176 ns                                                 | 113 ns: 1.56x faster                                  |
| go                      | 226 ms                                                 | 147 ms: 1.53x faster                                  |
| scimark_sor             | 197 ms                                                 | 129 ms: 1.53x faster                                  |
| nbody                   | 144 ms                                                 | 94.7 ms: 1.52x faster                                 |
| scimark_monte_carlo     | 109 ms                                                 | 72.6 ms: 1.50x faster                                 |
| richards                | 75.2 ms                                                | 50.8 ms: 1.48x faster                                 |
| pyflate                 | 676 ms                                                 | 459 ms: 1.47x faster                                  |
| raytrace                | 467 ms                                                 | 321 ms: 1.46x faster                                  |
| spectral_norm           | 150 ms                                                 | 104 ms: 1.43x faster                                  |
| chaos                   | 106 ms                                                 | 74.9 ms: 1.41x faster                                 |
| float                   | 109 ms                                                 | 77.5 ms: 1.40x faster                                 |
| mako                    | 14.7 ms                                                | 10.5 ms: 1.40x faster                                 |
| hexiom                  | 9.43 ms                                                | 6.76 ms: 1.39x faster                                 |
| crypto_pyaes            | 117 ms                                                 | 83.8 ms: 1.39x faster                                 |
| logging_format          | 8.85 us                                                | 6.37 us: 1.39x faster                                 |
| logging_simple          | 8.10 us                                                | 5.84 us: 1.39x faster                                 |
| pickle_pure_python      | 452 us                                                 | 334 us: 1.35x faster                                  |
| scimark_lu              | 161 ms                                                 | 120 ms: 1.34x faster                                  |
| chameleon               | 9.17 ms                                                | 6.95 ms: 1.32x faster                                 |
| django_template         | 46.3 ms                                                | 35.4 ms: 1.31x faster                                 |
| xml_etree_process       | 74.5 ms                                                | 57.0 ms: 1.31x faster                                 |
| unpack_sequence         | 59.4 ns                                                | 46.0 ns: 1.29x faster                                 |
| pycparser               | 1.53 sec                                               | 1.19 sec: 1.28x faster                                |
| thrift                  | 1.03 ms                                                | 815 us: 1.27x faster                                  |
| regex_compile           | 177 ms                                                 | 140 ms: 1.26x faster                                  |
| html5lib                | 85.9 ms                                                | 67.9 ms: 1.26x faster                                 |
| 2to3                    | 335 ms                                                 | 267 ms: 1.26x faster                                  |
| fannkuch                | 488 ms                                                 | 400 ms: 1.22x faster                                  |
| scimark_fft             | 421 ms                                                 | 347 ms: 1.21x faster                                  |
| tornado_http            | 128 ms                                                 | 106 ms: 1.21x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 249 us: 1.21x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 79.6 ms: 1.18x faster                                 |
| dulwich_log             | 75.8 ms                                                | 65.7 ms: 1.15x faster                                 |
| nqueens                 | 100 ms                                                 | 87.2 ms: 1.15x faster                                 |
| sympy_integrate         | 24.0 ms                                                | 21.3 ms: 1.13x faster                                 |
| json                    | 5.35 ms                                                | 4.84 ms: 1.10x faster                                 |
| json_dumps              | 13.4 ms                                                | 12.2 ms: 1.10x faster                                 |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                  |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                 |
| sqlite_synth            | 2.92 us                                                | 2.71 us: 1.08x faster                                 |
| sympy_sum               | 183 ms                                                 | 170 ms: 1.08x faster                                  |
| json_loads              | 28.7 us                                                | 26.7 us: 1.07x faster                                 |
| sympy_str               | 325 ms                                                 | 304 ms: 1.07x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 153 ms: 1.07x faster                                  |
| sympy_expand            | 534 ms                                                 | 503 ms: 1.06x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 5.14 ms: 1.06x faster                                 |
| pickle_list             | 4.72 us                                                | 4.47 us: 1.06x faster                                 |
| unpickle                | 14.2 us                                                | 13.4 us: 1.05x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.04x faster                                  |
| regex_v8                | 25.0 ms                                                | 24.0 ms: 1.04x faster                                 |
| pickle                  | 10.2 us                                                | 9.93 us: 1.02x faster                                 |
| regex_effbot            | 3.19 ms                                                | 3.14 ms: 1.02x faster                                 |
| regex_dna               | 214 ms                                                 | 213 ms: 1.01x faster                                  |
| pickle_dict             | 27.6 us                                                | 28.1 us: 1.02x slower                                 |
| python_startup_no_site  | 5.78 ms                                                | 5.92 ms: 1.02x slower                                 |
| unpickle_list           | 4.92 us                                                | 5.26 us: 1.07x slower                                 |
| Geometric mean          | (ref)                                                  | 1.23x faster                                          |

Benchmark hidden because not significant (2): telco, pidigits
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
