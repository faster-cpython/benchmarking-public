
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 335 ms                                                 | 256 ms: 1.31x faster                                  |
| chameleon      | 9.17 ms                                                | 6.59 ms: 1.39x faster                                 |
| html5lib       | 85.9 ms                                                | 63.8 ms: 1.35x faster                                 |
| tornado_http   | 128 ms                                                 | 93.8 ms: 1.37x faster                                 |
| Geometric mean | (ref)                                                  | 1.35x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 144 ms                                                 | 90.9 ms: 1.58x faster                                 |
| float          | 109 ms                                                 | 72.8 ms: 1.50x faster                                 |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.33x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                  |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.16x faster                                 |
| regex_dna      | 214 ms                                                 | 196 ms: 1.09x faster                                  |
| regex_effbot   | 3.19 ms                                                | 3.02 ms: 1.06x faster                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 302 us: 1.50x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.3 ms: 1.40x faster                                 |
| unpickle_pure_python | 302 us                                                 | 227 us: 1.33x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 75.8 ms: 1.24x faster                                 |
| json_loads           | 28.7 us                                                | 24.3 us: 1.18x faster                                 |
| pickle_list          | 4.72 us                                                | 4.30 us: 1.10x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                  |
| json_dumps           | 13.4 ms                                                | 12.6 ms: 1.07x faster                                 |
| pickle_dict          | 27.6 us                                                | 25.9 us: 1.07x faster                                 |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                 |
| pickle               | 10.2 us                                                | 9.61 us: 1.06x faster                                 |
| xml_etree_parse      | 163 ms                                                 | 157 ms: 1.04x faster                                  |
| unpickle_list        | 4.92 us                                                | 4.98 us: 1.01x slower                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.33 ms: 1.69x faster                                 |
| python_startup_no_site | 5.78 ms                                                | 6.17 ms: 1.07x slower                                 |
| Geometric mean         | (ref)                                                  | 1.26x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.71 ms: 1.51x faster                                 |
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                 |
| Geometric mean  | (ref)                                                  | 1.47x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-main-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.60 ms: 2.02x faster                                 |
| logging_silent          | 176 ns                                                 | 98.1 ns: 1.80x faster                                 |
| scimark_sor             | 197 ms                                                 | 115 ms: 1.71x faster                                  |
| python_startup          | 14.1 ms                                                | 8.33 ms: 1.69x faster                                 |
| richards                | 75.2 ms                                                | 45.3 ms: 1.66x faster                                 |
| go                      | 226 ms                                                 | 136 ms: 1.65x faster                                  |
| pyflate                 | 676 ms                                                 | 410 ms: 1.65x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 66.5 ms: 1.63x faster                                 |
| raytrace                | 467 ms                                                 | 291 ms: 1.60x faster                                  |
| nbody                   | 144 ms                                                 | 90.9 ms: 1.58x faster                                 |
| crypto_pyaes            | 117 ms                                                 | 73.8 ms: 1.58x faster                                 |
| chaos                   | 106 ms                                                 | 67.8 ms: 1.56x faster                                 |
| spectral_norm           | 150 ms                                                 | 96.3 ms: 1.55x faster                                 |
| mako                    | 14.7 ms                                                | 9.71 ms: 1.51x faster                                 |
| pickle_pure_python      | 452 us                                                 | 302 us: 1.50x faster                                  |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                  |
| float                   | 109 ms                                                 | 72.8 ms: 1.50x faster                                 |
| hexiom                  | 9.43 ms                                                | 6.32 ms: 1.49x faster                                 |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                 |
| xml_etree_process       | 74.5 ms                                                | 53.3 ms: 1.40x faster                                 |
| logging_simple          | 8.10 us                                                | 5.82 us: 1.39x faster                                 |
| chameleon               | 9.17 ms                                                | 6.59 ms: 1.39x faster                                 |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                |
| logging_format          | 8.85 us                                                | 6.42 us: 1.38x faster                                 |
| unpack_sequence         | 59.4 ns                                                | 43.2 ns: 1.38x faster                                 |
| thrift                  | 1.03 ms                                                | 756 us: 1.37x faster                                  |
| tornado_http            | 128 ms                                                 | 93.8 ms: 1.37x faster                                 |
| html5lib                | 85.9 ms                                                | 63.8 ms: 1.35x faster                                 |
| unpickle_pure_python    | 302 us                                                 | 227 us: 1.33x faster                                  |
| 2to3                    | 335 ms                                                 | 256 ms: 1.31x faster                                  |
| regex_compile           | 177 ms                                                 | 136 ms: 1.30x faster                                  |
| scimark_fft             | 421 ms                                                 | 324 ms: 1.30x faster                                  |
| fannkuch                | 488 ms                                                 | 394 ms: 1.24x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 75.8 ms: 1.24x faster                                 |
| nqueens                 | 100 ms                                                 | 82.4 ms: 1.21x faster                                 |
| dulwich_log             | 75.8 ms                                                | 62.6 ms: 1.21x faster                                 |
| json_loads              | 28.7 us                                                | 24.3 us: 1.18x faster                                 |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.18x faster                                 |
| sqlite_synth            | 2.92 us                                                | 2.50 us: 1.17x faster                                 |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.16x faster                                 |
| sympy_sum               | 183 ms                                                 | 159 ms: 1.15x faster                                  |
| sympy_expand            | 534 ms                                                 | 465 ms: 1.15x faster                                  |
| sympy_str               | 325 ms                                                 | 284 ms: 1.14x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.79 ms: 1.14x faster                                 |
| json                    | 5.35 ms                                                | 4.72 ms: 1.13x faster                                 |
| pickle_list             | 4.72 us                                                | 4.30 us: 1.10x faster                                 |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                 |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                  |
| regex_dna               | 214 ms                                                 | 196 ms: 1.09x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                  |
| json_dumps              | 13.4 ms                                                | 12.6 ms: 1.07x faster                                 |
| pickle_dict             | 27.6 us                                                | 25.9 us: 1.07x faster                                 |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                 |
| regex_effbot            | 3.19 ms                                                | 3.02 ms: 1.06x faster                                 |
| pickle                  | 10.2 us                                                | 9.61 us: 1.06x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 157 ms: 1.04x faster                                  |
| telco                   | 6.73 ms                                                | 6.64 ms: 1.01x faster                                 |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                  |
| unpickle_list           | 4.92 us                                                | 4.98 us: 1.01x slower                                 |
| python_startup_no_site  | 5.78 ms                                                | 6.17 ms: 1.07x slower                                 |
| Geometric mean          | (ref)                                                  | 1.30x faster                                          |
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
