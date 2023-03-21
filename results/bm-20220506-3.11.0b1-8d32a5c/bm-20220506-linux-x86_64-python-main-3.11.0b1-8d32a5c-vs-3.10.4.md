
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 335 ms                                                 | 256 ms: 1.31x faster                                  |
| chameleon      | 9.17 ms                                                | 6.57 ms: 1.40x faster                                 |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                 |
| tornado_http   | 128 ms                                                 | 94.6 ms: 1.35x faster                                 |
| Geometric mean | (ref)                                                  | 1.37x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.1 ms: 1.55x faster                                 |
| float          | 109 ms                                                 | 72.5 ms: 1.50x faster                                 |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.32x faster                                  |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                 |
| regex_effbot   | 3.19 ms                                                | 2.93 ms: 1.09x faster                                 |
| regex_dna      | 214 ms                                                 | 204 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 305 us: 1.48x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.6 ms: 1.39x faster                                 |
| unpickle_pure_python | 302 us                                                 | 229 us: 1.32x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.5 ms: 1.23x faster                                 |
| json_loads           | 28.7 us                                                | 25.4 us: 1.13x faster                                 |
| pickle_list          | 4.72 us                                                | 4.26 us: 1.11x faster                                 |
| json_dumps           | 13.4 ms                                                | 12.4 ms: 1.09x faster                                 |
| pickle_dict          | 27.6 us                                                | 25.6 us: 1.08x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.06x faster                                  |
| pickle               | 10.2 us                                                | 9.56 us: 1.06x faster                                 |
| unpickle             | 14.2 us                                                | 13.4 us: 1.06x faster                                 |
| xml_etree_parse      | 163 ms                                                 | 157 ms: 1.04x faster                                  |
| unpickle_list        | 4.92 us                                                | 5.05 us: 1.03x slower                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.25 ms: 1.71x faster                                 |
| python_startup_no_site | 5.78 ms                                                | 6.16 ms: 1.07x slower                                 |
| Geometric mean         | (ref)                                                  | 1.27x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.88 ms: 1.48x faster                                 |
| django_template | 46.3 ms                                                | 32.8 ms: 1.41x faster                                 |
| Geometric mean  | (ref)                                                  | 1.45x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.61 ms: 2.02x faster                                 |
| logging_silent          | 176 ns                                                 | 98.2 ns: 1.80x faster                                 |
| scimark_sor             | 197 ms                                                 | 115 ms: 1.72x faster                                  |
| python_startup          | 14.1 ms                                                | 8.25 ms: 1.71x faster                                 |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                  |
| pyflate                 | 676 ms                                                 | 411 ms: 1.65x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 66.5 ms: 1.63x faster                                 |
| richards                | 75.2 ms                                                | 46.4 ms: 1.62x faster                                 |
| raytrace                | 467 ms                                                 | 294 ms: 1.59x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 74.3 ms: 1.57x faster                                 |
| nbody                   | 144 ms                                                 | 93.1 ms: 1.55x faster                                 |
| chaos                   | 106 ms                                                 | 68.6 ms: 1.54x faster                                 |
| spectral_norm           | 150 ms                                                 | 97.6 ms: 1.53x faster                                 |
| float                   | 109 ms                                                 | 72.5 ms: 1.50x faster                                 |
| hexiom                  | 9.43 ms                                                | 6.29 ms: 1.50x faster                                 |
| mako                    | 14.7 ms                                                | 9.88 ms: 1.48x faster                                 |
| pickle_pure_python      | 452 us                                                 | 305 us: 1.48x faster                                  |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.47x faster                                  |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                 |
| django_template         | 46.3 ms                                                | 32.8 ms: 1.41x faster                                 |
| chameleon               | 9.17 ms                                                | 6.57 ms: 1.40x faster                                 |
| thrift                  | 1.03 ms                                                | 741 us: 1.39x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 53.6 ms: 1.39x faster                                 |
| logging_simple          | 8.10 us                                                | 5.89 us: 1.38x faster                                 |
| logging_format          | 8.85 us                                                | 6.44 us: 1.37x faster                                 |
| tornado_http            | 128 ms                                                 | 94.6 ms: 1.35x faster                                 |
| unpack_sequence         | 59.4 ns                                                | 44.3 ns: 1.34x faster                                 |
| unpickle_pure_python    | 302 us                                                 | 229 us: 1.32x faster                                  |
| regex_compile           | 177 ms                                                 | 135 ms: 1.32x faster                                  |
| 2to3                    | 335 ms                                                 | 256 ms: 1.31x faster                                  |
| scimark_fft             | 421 ms                                                 | 325 ms: 1.30x faster                                  |
| pycparser               | 1.53 sec                                               | 1.18 sec: 1.29x faster                                |
| fannkuch                | 488 ms                                                 | 385 ms: 1.27x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 76.5 ms: 1.23x faster                                 |
| dulwich_log             | 75.8 ms                                                | 62.8 ms: 1.21x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.57 ms: 1.19x faster                                 |
| nqueens                 | 100 ms                                                 | 84.7 ms: 1.18x faster                                 |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.18x faster                                 |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                 |
| sqlite_synth            | 2.92 us                                                | 2.53 us: 1.16x faster                                 |
| sympy_str               | 325 ms                                                 | 284 ms: 1.15x faster                                  |
| sympy_expand            | 534 ms                                                 | 468 ms: 1.14x faster                                  |
| sympy_sum               | 183 ms                                                 | 161 ms: 1.14x faster                                  |
| json_loads              | 28.7 us                                                | 25.4 us: 1.13x faster                                 |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                 |
| pickle_list             | 4.72 us                                                | 4.26 us: 1.11x faster                                 |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                  |
| regex_effbot            | 3.19 ms                                                | 2.93 ms: 1.09x faster                                 |
| json                    | 5.35 ms                                                | 4.91 ms: 1.09x faster                                 |
| json_dumps              | 13.4 ms                                                | 12.4 ms: 1.09x faster                                 |
| pickle_dict             | 27.6 us                                                | 25.6 us: 1.08x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.06x faster                                  |
| pickle                  | 10.2 us                                                | 9.56 us: 1.06x faster                                 |
| unpickle                | 14.2 us                                                | 13.4 us: 1.06x faster                                 |
| regex_dna               | 214 ms                                                 | 204 ms: 1.05x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 157 ms: 1.04x faster                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                  |
| telco                   | 6.73 ms                                                | 6.84 ms: 1.02x slower                                 |
| unpickle_list           | 4.92 us                                                | 5.05 us: 1.03x slower                                 |
| python_startup_no_site  | 5.78 ms                                                | 6.16 ms: 1.07x slower                                 |
| Geometric mean          | (ref)                                                  | 1.30x faster                                          |
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
